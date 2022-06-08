message = [{
    "id": "abc",
    "act": "box.validate_camera",
    "arg": {"uri": "rtsp://qq.com", "hd_uri": "rtsp://qq.com", "box_id": "box_dog_sr_50006", "username": "user",
            "password": "password"}
}, {
    "id": "abc",
    "act": "box.validate_dvr",
    "arg": {"host": "qq.com", "box_id": "box_dog_sr_50006", "username": "user", "password": "password",
            "mac_address": "3c:ef:8c:44:55:66:77:88", "channels": 4}
}, {
    "id": "abc",
    "act": "box.camera.start_stream",
    "arg": {"camera_id": 1}
}, {
    "id": "abc",
    "act": "box.camera.capture_case",
    "arg": {"case_id": 130}
}, {
    "id": "abc",
    "act": "stream.stop",
    "arg": {"uri": "rtsp://qq.com", "box_id": "box_dog_sr_50006", "username": "user", "password": "password"}
}, {
    "id": "abc",
    "act": "box.camera.save_video",
    "arg": {"camera_id": 2, "started_at": "2020-01-16T06:17:56.262076Z", "ended_at": "2020-01-16T06:17:57.262076Z"}
}, {
    "id": "abc",
    "act": "box.search",
    "arg": {"box_id": "box_dog_sr_50006"}
}, {
    "id": "abc",
    "act": "box.debug_echo",
    "arg": {"box_id": "box_dog_sr_50006"}
}, {
    "id": "abc",
    "act": "box.camera.set_camera_config",
    "arg": {"camera_id": 1, "outdoor": "false", "low": 34.0, "high": 45.0, "abnormal": 36.5}
}, {
    "id": "abc",
    "act": "box.camera.get_camera_config",
    "arg": {"camera_id": 1}
}, {
    #     "id": "abc",
    #     "act": "box.systemctl_restart",
    #     "arg": {"box_id": "box_dog_sr_50006", "service": "zenod"}
    # }, {
    "id": "abc",
    "act": "robot.setup",
    "arg": {"robot_id": "robot_dog_sr_20002", "ip_address": "127.0.0.1"}
}, {
    "id": "abc",
    "act": "robot.move",
    "arg": {"robot_id": "robot_dog_sr_20002", "x": 0.0, "y": 0.0, "ip_address": "192.168.3.48"}
}, {
    "id": "abc",
    "act": "robot.start_stream",
    "arg": {"robot_id": "robot_dog_sr_20002", "camera": "front"}
}, {
    "id": "abc",
    "act": "robot.play_sound",
    "arg": {"robot_id": "robot_dog_sr_20002"}
}, {
    "id": "abc",
    "act": "robot.switch_mode",
    "arg": {"robot_id": "robot_dog_sr_20002", "mode": "patrol"}
}, {
    "id": "abc",
    "act": "robot.comm_play",
    "arg": {"robot_id": "robot_dog_sr_20002", "data": "dGVzdA=="}
}, {
    "id": "abc",
    "act": "robot.search_macs",
    "arg": {"robot_id": "robot_dog_sr_20002"}
}, {
    "id": "abc",
    "act": "robot.directive.react",
    "arg": {"robot_id": "robot_dog_sr_20002", "event_id": 92}
}, {
    "id": "abc",
    "act": "robot.directive.investigate",
    "arg": {"robot_id": "robot_dog_sr_20002", "location": {"lat": 0, "lng": 0}}
}, {
    "id": "abc",
    "act": "robot.go_home",
    "arg": {"robot_id": "robot_dog_sr_20002"}
}, {
    "id": "abc",
    "act": "robot.leave_home",
    "arg": {"robot_id": "robot_dog_sr_20002"}
}, {
    "id": "abc",
    "act": "robot.systemctl_restart",
    "arg": {"robot_id": "robot_dog_sr_20002", "service": "zenod"}
}, {
    "id": "abc",
    "act": "robot.map_upload",
    "arg": {"robot_id": "robot_dog_sr_20002"}
}, {
    "id": "abc",
    "act": "robot.download_map",
    "arg": {"robot_id": "robot_dog_sr_20002", "map_id": "ss", "files": [{"file": {"url": "test.com"}, "type": "image"}]}
}, {
    "id": "abc",
    "act": "robot.reset_slam",
    "arg": {"robot_id": "robot_dog_sr_20002", "pose": {"x": 0, "y": 0, "theta": 0}}
}, {
    "id": "abc",
    "act": "wisp.view_robot",
    "arg": {"robot_id": "robot_dog_sr_20002", "camera": "front"}
}, {
    "id": "abc",
    "act": "wisp.present_to_robot",
    "arg": {"robot_id": "robot_dog_sr_20002"}
}, {
    "id": "abc",
    "act": "robot.micro_move",
    "arg": {"robot_id": "robot_dog_sr_20002", "distance": 0, "angle": 0}
}, {
    "id": "abc",
    "act": "robot.systemctl_start",
    "arg": {"robot_id": "robot_test_10001", "service": "zenod"}
}, {
    "id": "abc",
    "act": "robot.systemctl_restart",
    "arg": {"robot_id": "robot_test_10001", "service": "zenod"}
}, {
    "id": "abc",
    "act": "robot.systemctl_stop",
    "arg": {"robot_id": "robot_test_10001", "service": "zenod"}
}, {
    "id": "abc",
    "act": "robot.lift_callback",
    "arg": {
        "robot_id": "robot_test_10001"
    }
}, {
    "id": "abc",
    "act": "robot.complete_routine",
    "arg": {"robot_id": "robot_test_10001"}
}, {
    "id": "abc",
    "act": "robot.switch_mode",
    "arg": {"robot_id": "robot_test_10001", "mode": "idle"}
}, {
    "id": "abc",
    "act": "robot.pause_routine",
    "arg": {"robot_id": "robot_test_10001", "routine_execution_id": "test"}
}, {
    "id": "abc",
    "act": "robot.resume_routine",
    "arg": {"robot_id": "robot_test_10001", "routine_execution_id": "", "next_action": ""}
}
]
