# Robot video streaming
websocket interface
## Authentication
User login, get token.

URL: https://dev-guard.turingvideo.cn/auth/
Method: POST
Input:
```json
{
    "username": "test@turingvideo.net",
    "password": "*********"
} 

```
Output:
```json
{
	"err": {
		"ec": 0,
		"em": "ok"
	},
	"ret": {
		"token": "sssswqwe12321dwadsadsadas",
		"expire": "2020-05-09 14:35:41.748447+08"
	},
	"ext": null,
	"ebd": null
}

```

## websocket
The robot real-time video websocket interface is `wss://dev-api.turingvideo.cn:8443/channel/app`

### connect
```python
 async with websockets.connect(paths, extra_headers=cookie) as websocket:
        conn = WebSocketService(websocket)
```
| param               | explanation                                         |
| ---------------------- | ------------------------------------------- |
| `paths`  | wss://dev-api.turingvideo.cn:8443/channel/app  |
| `cookie` |     As parameter: tonken = *** （or） As header: Authorization: 'Bearer ***' |

`***` is `token` value.
### start stream
```python
        await conn.s_send(message)
```
Input(`message`) format:
```json
{
    "id": "abc",
    "act": "robot.start_stream",
    "arg": {"robot_id": "robot_dog_sr_20002", "camera": "front"}
}
```
|       params           | explanation                                 |
| ---------------------- | ------------------------------------------- |
|       robot_id         |   View robot_id of live video     |   
|       camera           |   Robot name       |

Output:
```json
{
	"id": "abc",
	"act": "robot.start_stream!",
	"err": {
		"ec": 0,
		"em": "This operation is successful.",
		"dm": "ok"
	},
	"ret": {
		"uri": "rtsp://stream.tucingcideo.cn",
		"hls_uri": "rtsp://stream.tucingcideo.cn"
	}
}
```
### Fetch HLS
URL: https://dev-hls.turingvideo.cn/stream/

Method: POST

Authorization:

    * As parameter: tonken = ****
    * As header: Authorization: 'Bearer cG******'
    
Input:
    
```json
{
    "id": "robot_dog_sr_10001",
    "rtsp_url": "rtsp://stream.tucingcideo.cn"
} 
// `rtsp_url` is the value returned by` robot.start_stream`
```
Output:
```json
	"err": {
		"ec": 0,
		"em": "ok"
	},
	"ret": {
		"hls_url": "https://dev-hls.tucingcideo.cn/videos/robot_dog_sr_10001/index.m3u8"
	},
	"ext": null,
	"ebd": null
```

Open the `hls_url` in the local browser to view the video stream