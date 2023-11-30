// A script that connects to Redis server
import { createClient } from 'redis';

function redisConnect() {
  const client = createClient();

  client.on('connect', function() {
    console.log('Redis client connect to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

};

redisConnect();
