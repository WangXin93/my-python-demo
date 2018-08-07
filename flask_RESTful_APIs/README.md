# Home Automation Device Registry (Flask RESTful APIs)

## Requiements

- docker.io
- docker-compose

Python libraries are listed in `requirements.txt`.

### Running
You can start the device registry by typing `docker-compose up`. The service will be available at port 8888. If you changed docker image for example `Dockerfile` or `docker-compose.yml`, typing `docker-compose build` then type `docker-compose up`.

Use `curl localhost:8888` to browse that in CLI.

You can use `docker inspect container_ID` to get IP address to communicate with container. It can also be automatically done in the following way:
```
CN="sharp_bartik"
CIP=$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' $CN)
curl  http://$CIP
```
You can also retrieve all containers and their IP address:
```
sudo docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(sudo docker ps -aq)
```

## Usage
All responses will have the form:

```json
{
    "message": "Description of what happened",
    "data": "Mixed type holding the content of the response"
}
```

Subsequent response definitions will only detail the expected value of the `data` field.

### List all devices
**Definition**

`GET /devices`

**Response**

- 200: success

```json
[
    {
        "identifier": "id1",
        "name": "Device 1",
        "device_type": "switch",
        "controller_name": "controller-1",
    },
    {
        "identifier": "id2",
        "name": "Device 2",
        "device_type": "bulb",
        "controller_name": "controller-2",
    }
]
```

### Register a new device
**Definition**

`POST /devices`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for the device
- `"device_type":string` the type of the device as understood by the client
- `"controller_name":string` the name of the device's controller

If the identifier already exists, the existing device will be overwritten.

**Response**

- 400: unknown room
- 201: created successfully

Returns the new device if successful.

```json
{
    "identifier": "id1",
    "name": "Device 1",
    "device_type": "switch",
    "controller_name": "controller-2",
}
```

### Lookup device details
**Definition**

`GET /device/<identifier>`

**Response**

- 404: device not found
- 200: success

```json
{
    "identifier": "id1",
    "name": "Device 1",
    "device_type": "switch",
    "controller_name": "controller-1",
}
```

### Delete a device
**Definition**

`DELETE /device/<identifier>`

**Response**

- 404: device not found
- 204: success

# 参考
- 视频链接：https://www.youtube.com/watch?v=4T5Gnrmzjak
- 对应项目：https://github.com/jakewright/home-automation
