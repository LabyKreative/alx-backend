// A script to create a job notification
import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  'phoneNumber': '8012345678',
  'message': 'Verify your account with this code'
}

const job = queue.create('push_notification_code', notification).save(function (error) {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', function() {
    console.log('Notification job completed');
}).on('failed', function() {
    console.log('Notification job failed');
});
