// src/script.test.js

import { JSDOM } from 'jsdom';
import fetchMock from 'jest-fetch-mock';

// Setup a mock DOM environment
const dom = new JSDOM(`<!DOCTYPE html><html><body>
  <form id="login-form">
    <input id="username" type="text" />
    <input id="password" type="password" />
    <input id="csrf-token" type="hidden" />
    <div id="error-message"></div>
  </form>
</body></html>`);
globalThis.document = dom.window.document;
globalThis.window = dom.window;

// Mock the fetch API
fetchMock.enableMocks();

describe('Login Form', () => {
  beforeEach(() => {
    // Reset the form and error message before each test
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
    document.getElementById('error-message').innerText = '';
  });

  afterEach(() => {
    // Clear the fetch mock after each test
    fetchMock.resetMocks();
  });

  // Happy path
  it('should submit the form with valid credentials', async () => {
    // Arrange
    const username = 'testUser';
    const password = 'TestP@ssw0rd';
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;
    fetchMock.mockResponseOnce(JSON.stringify({ success: true }));

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(fetchMock).toHaveBeenCalledWith('https://your-website.com/api/login', expect.objectContaining({
      method: 'POST',
      headers: expect.objectContaining({
        'Content-Type': 'application/json',
        'X-CSRF-Token': expect.any(String),
      }),
      body: JSON.stringify({ username, password }),
    }));
  });

  // Edge cases
  it('should display an error message for empty username', async () => {
    // Arrange
    const password = 'TestP@ssw0rd';
    document.getElementById('password').value = password;

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(document.getElementById('error-message').innerText).toBe('Please fill in all fields.');
  });

  it('should display an error message for empty password', async () => {
    // Arrange
    const username = 'testUser';
    document.getElementById('username').value = username;

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(document.getElementById('error-message').innerText).toBe('Please fill in all fields.');
  });

  it('should display an error message for invalid username', async () => {
    // Arrange
    const username = 'a';
    const password = 'TestP@ssw0rd';
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(document.getElementById('error-message').innerText).toBe('Username should be between 3 and 16 characters long and contain only letters, numbers, and underscores.');
  });

  it('should display an error message for invalid password', async () => {
    // Arrange
    const username = 'testUser';
    const password = 'password';
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(document.getElementById('error-message').innerText).toBe('Password should be at least 8 characters long, contain at least one lowercase letter, one uppercase letter, one number, and one special character.');
  });

  // Error cases
  it('should display an error message for invalid username or password', async () => {
    // Arrange
    const username = 'testUser';
    const password = 'TestP@ssw0rd';
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;
    fetchMock.mockResponseOnce(JSON.stringify({ success: false }));

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(document.getElementById('error-message').innerText).toBe('Invalid username or password.');
  });

  it('should display an error message for fetch error', async () => {
    // Arrange
    const username = 'testUser';
    const password = 'TestP@ssw0rd';
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;
    fetchMock.mockReject(new Error('Fetch error'));

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(document.getElementById('error-message').innerText).toBe('An error occurred while logging in.');
  });

  // Security cases
  it('should prevent CSRF token injection', async () => {
    // Arrange
    const username = 'testUser';
    const password = 'TestP@ssw0rd';
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;
    const csrfToken = document.getElementById('csrf-token');
    csrfToken.value = 'malicious-token';

    // Act
    const form = document.getElementById('login-form');
    const submitEvent = new dom.window.Event('submit');
    form.dispatchEvent(submitEvent);

    // Assert
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(fetchMock).toHaveBeenCalledWith('https://your-website.com/api/login', expect.objectContaining({
      method: 'POST',
      headers: expect.objectContaining({
        'Content-Type': 'application/json',
        'X-CSRF-Token': expect.any(String),
      }),
      body: JSON.stringify({ username, password }),
    }));
  });
});