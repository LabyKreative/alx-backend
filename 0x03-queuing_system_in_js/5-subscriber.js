// A script that connects to Redis server & subscribe to the specified channel
import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
});

redisClient.on('error', function (error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

// subscribes to holberton school channel
redisClient.subscribe('holberton school channel');

// listens for messages on channel and print it when received
redisClient.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
// to unsubscribe from channel and close the server connection
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
