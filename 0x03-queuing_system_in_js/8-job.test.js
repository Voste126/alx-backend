import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter(); // Enter test mode to avoid actual job processing
  });

  afterEach(() => {
    queue.testMode.clear(); // Clear the queue after each test
    queue.testMode.exit();  // Exit test mode
  });

  it('should display an error message if jobs is not an array', () => {
    const invalidInput = {};

    expect(() => createPushNotificationsJobs(invalidInput, queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Hello, User 1!' },
      { phoneNumber: '9876543210', message: 'Hello, User 2!' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2); // Validate number of jobs
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3'); // Validate type
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]); // Validate job data
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
