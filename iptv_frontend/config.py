WORKER={
    "host":"https://localhost:8888",
    "worker":{
        "1":"/api/v1/ctl/127.0.0.1/master/start-worker",
        "0":"/api/v1/ctl/127.0.0.1/master/stop-worker",
    },
    "signal":{
        1:"/api/v1/ctl/127.0.0.1/master/signal/enable",
        0:"/api/v1/ctl/127.0.0.1/master/signal/disable",
    },
    "video" : {
        1:"/api/v1/ctl/127.0.0.1/master/video/enable",
        0:"/api/v1/ctl/127.0.0.1/master/video/disable",
    },
    "audio": {
        1:"/api/v1/ctl/127.0.0.1/master/audio/enable",
        0:"/api/v1/ctl/127.0.0.1/master/audio/disable",
    },
   "thread":"/api/v1/ctl/127.0.0.1/master/start-worker"
}