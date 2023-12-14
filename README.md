## Hrextension

An Extension for hrms

#### License

MIT

## Installation

### Manual Installation

1. [Install bench](https://github.com/frappe/bench).
2. [Install ERPNext](https://github.com/frappe/erpnext#installation).
3. Once ERPNext is installed, add the hrextension app to your bench by running

	```sh
	$ bench get-app https://github.com/kimoamer/hrextension
	```
4. After that, you can install the hrextension app on the required site by running
	```sh
	$ bench --site sitename install-app hrextension
	```
 5. Build app
    ```sh
  	$ bench build --app hrextension
  	```
