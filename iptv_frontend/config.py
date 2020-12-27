WORKER={
    "host":"http://localhost:8888",
    "worker":{
        "1":"/api/v1/ctl/127.0.0.1/master/start-worker",
        "0":"/api/v1/ctl/127.0.0.1/master/stop-worker",
    },
    "signal":{
        "1":"/api/v1/ctl/127.0.0.1/master/monitor/signal/enable",
        "0":"/api/v1/ctl/127.0.0.1/master/monitor/signal/disable",
    },
    "video" : {
        "1":"/api/v1/ctl/127.0.0.1/master/monitor/video/enable",
        "0":"/api/v1/ctl/127.0.0.1/master/monitor/video/disable",
    },
    "audio": {
        "1":"/api/v1/ctl/127.0.0.1/master/monitor/audio/enable",
        "0":"/api/v1/ctl/127.0.0.1/master/monitor/audio/disable",
    },
   "thread":"/api/v1/ctl/127.0.0.1/master/monitor/start-worker"
}