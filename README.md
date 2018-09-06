# chaostoolkit-turbulence

This is an extension for [Chaos Toolkit](https://chaostoolkit.org/) which adds support for
[Turbulence](https://github.com/cppforlife/turbulence-release) attacks.

## Setup

### Install
To be used from your experiment, this package must first be installed in the Python environment where
[chaostoolkit](https://chaostoolkit.org/) already exists. This package requires at least
[Python](https://www.python.org/) version 3.5, so translate `python` as `python3` or `pyhton3.5` as appropriate for your
operating system.

From within the source, run:  

```bash
sudo python setup.py install
```

Or to install for just your user:  

```bash
python setup.py install --user
```

Now you should be able to import the package.

```python
import chaosturbulence
print(chaosturbulence.__version__)
```

### Turbulence Deployment
Before this plugin can be used, you need to have [Turbulence](https://github.com/cppforlife/turbulence-release) deployed
in a [BOSH](https://github.com/cloudfoundry/bosh) environment and have the api accessible form your system. Once this is
ready, specify the needed information in the configuration section of the attack. See the
[docs](https://github.com/cppforlife/turbulence-release/blob/master/docs/config.md) for more information on
how to deploy Turbulence.

## Usage
If you have not installed the `chaosturbulence` package, then make sure you run Chaos Toolkit from this directory (the
root of this repository) using `pyhton -m chaostoolkit run exp.json` or else the `chaosturbulence` module will not be
found. Otherwise just use `chaos run exp.json` from any directory.

To use, you will need to specify in the configuration:

- `turb_api_url`: The URL of the Turbulence API which POST requests will be sent to. This should be in the form `https://user:password@address:port`.
- `turb_verify_ssl`: Whether the SSL certificate should be verified. It will default to `true`.
 
Then, to write an attack simply specify the task type and the selector to use. More information about the tasks and
selectors can be found in the
[Turbulence API docs](https://github.com/cppforlife/turbulence-release/blob/master/docs/api.md).

A sample experiment for Turbulence integration with Chaos Toolkit:

```json
{
    "version": "1.0.0",
    "title": "What is the impact of killing one random diego cell?",
    "description": "If a diego-cell dies, then it should be restarted automatically and any applications on it should be relocated temporarily",
    "tags": ["tls"],
    "steady-state-hypothesis": {
        "title": "Application responds",
        "probes": []
    },
	"configuration": {
		"turb_api_url": "https://turbulence:admin@10.244.0.35:8080",
		"turb_verify_ssl": false
	},
    "method": [
        {
			"type": "action",
			"name": "terminate-diego-cells",
			"provider": {
				"type": "python",
				"module": "chaosturbulence.actions",
				"func": "attack",
				"arguments": {
					"task": { "Type": "Kill" },
					"selector": {
						"Deployment": {"Name": "cf"},
						"Group": {"Name": "diego-cell"},
						"ID": {"Limit": 1}
					}
				}
			}
		}
    ],
    "rollbacks": []
}
```

Because Turbulence has its own rollbacks setup based on the `timeout`, you may want to set
`"pauses": {"after": timeout}` where timeout is a number of seconds and pauses is a field in an action object. You can
read more in the [experiment documentation](https://docs.chaostoolkit.org/reference/api/experiment/#action).