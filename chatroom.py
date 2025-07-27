<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎤💬 ChatHub Pro - Advanced Messaging Platform</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

```
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        height: 100vh;
        display: flex;
        overflow: hidden;
    }

    .app-container {
        display: flex;
        width: 100%;
        height: 100vh;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        box-shadow: 0 0 50px rgba(0, 0, 0, 0.2);
    }

    /* Sidebar */
    .sidebar {
        width: 300px;
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
        display: flex;
        flex-direction: column;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
    }

    .sidebar-header {
        padding: 20px;
        text-align: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }

    .sidebar-header h1 {
        font-size: 1.5em;
        margin-bottom: 10px;
    }

    .user-profile {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 15px 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin: 0 10px;
    }

    .user-avatar {
        width: 40px;
        height: 40px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
    }

    .user-info {
        flex: 1;
    }

    .username {
        font-weight: bold;
        font-size: 14px;
    }

    .user-status {
        font-size: 12px;
        opacity: 0.8;
    }

    .nav-tabs {
        padding: 20px 10px;
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .nav-tab {
        background: rgba(255, 255, 255, 0.1);
        border: none;
        color: white;
        padding: 12px 15px;
        border-radius: 8px;
        cursor: pointer;
        text-align: left;
        font-size: 14px;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s ease;
    }

    .nav-tab:hover {
        background: rgba(255, 255, 255, 0.2);
    }

    .nav-tab.active {
        background: rgba(255, 255, 255, 0.3);
        font-weight: bold;
    }

    .online-users {
        flex: 1;
        padding: 20px 10px;
        overflow-y: auto;
    }

    .online-users h3 {
        margin-bottom: 15px;
        padding: 0 10px;
        font-size: 14px;
        opacity: 0.9;
    }

    .user-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 10px;
        border-radius: 6px;
        margin-bottom: 5px;
        transition: background 0.2s ease;
    }

    .user-item:hover {
        background: rgba(255, 255, 255, 0.1);
    }

    .user-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4CAF50;
    }

    .user-dot.voice {
        background: #ff9800;
        animation: pulse 1.5s infinite;
    }

    /* Main Content */
    .main-content {
        flex: 1;
        display: flex;
        flex-direction: column;
        background: white;
    }

    .content-header {
        padding: 20px 30px;
        background: rgba(0, 0, 0, 0.02);
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .content-title {
        font-size: 1.3em;
        font-weight: bold;
        color: #333;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .content-actions {
        display: flex;
        gap: 10px;
    }

    .action-btn {
        background: #667eea;
        color: white;
        border: none;
        padding: 8px 15px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 12px;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .action-btn:hover {
        background: #5a6fd8;
        transform: translateY(-1px);
    }

    .action-btn.danger {
        background: #f44336;
    }

    .action-btn.danger:hover {
        background: #d32f2f;
    }

    .tab-content {
        display: none;
        flex: 1;
        flex-direction: column;
    }

    .tab-content.active {
        display: flex;
    }

    /* Login Screen */
    .login-screen {
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
    }

    .login-form {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        width: 400px;
        text-align: center;
    }

    .login-form h1 {
        color: #333;
        margin-bottom: 30px;
        font-size: 2em;
    }

    .form-group {
        margin-bottom: 20px;
        text-align: left;
    }

    .form-group label {
        display: block;
        margin-bottom: 8px;
        color: #333;
        font-weight: bold;
    }

    .form-group input {
        width: 100%;
        padding: 12px 15px;
        border: 2px solid #ddd;
        border-radius: 8px;
        font-size: 14px;
        transition: border-color 0.3s ease;
    }

    .form-group input:focus {
        outline: none;
        border-color: #667eea;
    }

    .login-btn {
        width: 100%;
        background: #667eea;
        color: white;
        border: none;
        padding: 15px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .login-btn:hover {
        background: #5a6fd8;
        transform: translateY(-1px);
    }

    .register-link {
        margin-top: 20px;
        color: #666;
    }

    .register-link a {
        color: #667eea;
        text-decoration: none;
        font-weight: bold;
    }

    /* Chat Messages */
    .messages-container {
        flex: 1;
        padding: 20px 30px;
        overflow-y: auto;
        scroll-behavior: smooth;
    }

    .message {
        display: flex;
        margin-bottom: 20px;
        animation: slideIn 0.3s ease;
    }

    .message.own {
        justify-content: flex-end;
    }

    .message-bubble {
        max-width: 60%;
        padding: 12px 16px;
        border-radius: 18px;
        position: relative;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .message.own .message-bubble {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    .message:not(.own) .message-bubble {
        background: #f1f3f4;
        color: #333;
    }

    .message-header {
        font-size: 12px;
        opacity: 0.8;
        margin-bottom: 4px;
        font-weight: 500;
    }

    .message-text {
        font-size: 14px;
        line-height: 1.4;
        word-wrap: break-word;
    }

    .message-time {
        font-size: 11px;
        opacity: 0.6;
        margin-top: 4px;
    }

    .message-image {
        max-width: 100%;
        max-height: 300px;
        border-radius: 12px;
        margin-top: 8px;
        cursor: pointer;
        transition: transform 0.2s ease;
    }

    .message-image:hover {
        transform: scale(1.02);
    }

    /* Input Area */
    .input-area {
        padding: 20px 30px;
        background: rgba(0, 0, 0, 0.02);
        border-top: 1px solid rgba(0, 0, 0, 0.1);
    }

    .input-container {
        display: flex;
        gap: 10px;
        align-items: flex-end;
    }

    .message-input {
        flex: 1;
        padding: 12px 15px;
        border: 2px solid #ddd;
        border-radius: 20px;
        font-size: 14px;
        resize: none;
        min-height: 20px;
        max-height: 100px;
        outline: none;
        transition: border-color 0.3s ease;
    }

    .message-input:focus {
        border-color: #667eea;
    }

    .input-actions {
        display: flex;
        gap: 8px;
    }

    .input-btn {
        background: #667eea;
        color: white;
        border: none;
        padding: 12px 15px;
        border-radius: 20px;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .input-btn:hover {
        background: #5a6fd8;
        transform: translateY(-1px);
    }

    .input-btn.secondary {
        background: #ff9800;
    }

    .input-btn.secondary:hover {
        background: #f57c00;
    }

    /* Voice Room */
    .voice-room {
        padding: 30px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }

    .voice-controls {
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        justify-content: center;
    }

    .voice-btn {
        background: #4CAF50;
        color: white;
        border: none;
        padding: 15px 25px;
        border-radius: 50px;
        cursor: pointer;
        font-size: 14px;
        font-weight: bold;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .voice-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .voice-btn.recording {
        background: #f44336;
        animation: pulse 1.5s infinite;
    }

    .voice-btn.disabled {
        background: #ccc;
        cursor: not-allowed;
    }

    .voice-participants {
        background: rgba(0, 0, 0, 0.05);
        padding: 20px;
        border-radius: 15px;
        width: 100%;
        max-width: 500px;
    }

    /* Settings */
    .settings-panel {
        padding: 30px;
    }

    .settings-group {
        margin-bottom: 30px;
    }

    .settings-group h3 {
        color: #333;
        margin-bottom: 15px;
        font-size: 16px;
    }

    .setting-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }

    .setting-item:last-child {
        border-bottom: none;
    }

    .setting-toggle {
        width: 50px;
        height: 24px;
        background: #ddd;
        border-radius: 12px;
        position: relative;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    .setting-toggle.active {
        background: #667eea;
    }

    .setting-toggle::after {
        content: '';
        position: absolute;
        top: 2px;
        left: 2px;
        width: 20px;
        height: 20px;
        background: white;
        border-radius: 50%;
        transition: transform 0.3s ease;
    }

    .setting-toggle.active::after {
        transform: translateX(26px);
    }

    /* Animations */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .app-container {
            flex-direction: column;
        }

        .sidebar {
            width: 100%;
            height: auto;
            order: 2;
        }

        .main-content {
            order: 1;
        }

        .login-form {
            width: 90%;
            padding: 30px 20px;
        }

        .messages-container {
            padding: 15px 20px;
        }

        .input-area {
            padding: 15px 20px;
        }

        .message-bubble {
            max-width: 85%;
        }
    }

    /* Image Modal */
    .image-modal {
        display: none;
        position: fixed;
        z-index: 2000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.9);
        animation: fadeIn 0.3s ease;
    }

    .image-modal img {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        max-width: 90%;
        max-height: 90%;
        border-radius: 8px;
    }

    .image-modal .close {
        position: absolute;
        top: 20px;
        right: 35px;
        color: white;
        font-size: 40px;
        font-weight: bold;
        cursor: pointer;
    }

    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        background: #667eea;
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transform: translateX(400px);
        transition: transform 0.3s ease;
        z-index: 1500;
    }

    .notification.show {
        transform: translateX(0);
    }
</style>
```

</head>
<body>
    <!-- Login Screen -->
    <div id="loginScreen" class="login-screen">
        <div class="login-form">
            <h1>🎤💬 ChatHub Pro</h1>
            <p style="color: #666; margin-bottom: 30px;">Advanced messaging platform with voice, images, and persistence</p>

```
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" placeholder="Enter your username" maxlength="20">
        </div>
        
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" placeholder="Enter your password">
        </div>
        
        <button class="login-btn" onclick="login()">
            🚀 Enter ChatHub Pro
        </button>
        
        <div class="register-link">
            <p>First time? Just pick a username and password to create an account!</p>
        </div>
    </div>
</div>

<!-- Main App -->
<div id="mainApp" class="app-container" style="display: none;">
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="sidebar-header">
            <h1>🎤💬 ChatHub Pro</h1>
            <div class="user-profile">
                <div class="user-avatar">👤</div>
                <div class="user-info">
                    <div class="username" id="currentUsername">User</div>
                    <div class="user-status" id="userStatus">Online</div>
                </div>
            </div>
        </div>

        <div class="nav-tabs">
            <button class="nav-tab active" onclick="switchTab('chat')" data-tab="chat">
                💬 Text Chat
            </button>
            <button class="nav-tab" onclick="switchTab('voice')" data-tab="voice">
                🎤 Voice Room
            </button>
            <button class="nav-tab" onclick="switchTab('settings')" data-tab="settings">
                ⚙️ Settings
            </button>
        </div>

        <div class="online-users">
            <h3>👥 Online Users (<span id="onlineCount">1</span>)</h3>
            <div id="usersList">
                <div class="user-item">
                    <div class="user-dot"></div>
                    <span>You</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Chat Tab -->
        <div id="chatTab" class="tab-content active">
            <div class="content-header">
                <div class="content-title">
                    💬 Text Chat
                    <span style="font-size: 12px; color: #666;">Real-time messaging</span>
                </div>
                <div class="content-actions">
                    <button class="action-btn" onclick="clearChat()">🗑️ Clear</button>
                    <button class="action-btn" onclick="exportChat()">📤 Export</button>
                    <button class="action-btn danger" onclick="logout()">🚪 Logout</button>
                </div>
            </div>

            <div class="messages-container" id="messagesContainer">
                <div class="message">
                    <div class="message-bubble">
                        <div class="message-header">🤖 System</div>
                        <div class="message-text">Welcome to ChatHub Pro! This is an advanced messaging platform with persistent storage, voice chat, and image sharing. Start chatting! 🚀</div>
                        <div class="message-time">Just now</div>
                    </div>
                </div>
            </div>

            <div class="input-area">
                <div class="input-container">
                    <textarea id="messageInput" class="message-input" placeholder="Type your message..." rows="1" maxlength="500"></textarea>
                    <div class="input-actions">
                        <input type="file" id="imageInput" accept="image/*" style="display: none;" onchange="handleImageSelect(event)">
                        <button class="input-btn secondary" onclick="document.getElementById('imageInput').click()">
                            📸 Image
                        </button>
                        <button class="input-btn" onclick="sendMessage()">
                            📤 Send
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Voice Tab -->
        <div id="voiceTab" class="tab-content">
            <div class="content-header">
                <div class="content-title">
                    🎤 Voice Room
                    <span style="font-size: 12px; color: #666;">Push-to-talk voice chat</span>
                </div>
                <div class="content-actions">
                    <span id="connectionStatus" style="color: #666; font-size: 12px;">🔌 Connecting...</span>
                </div>
            </div>

            <div class="voice-room">
                <div id="voiceStatus" style="font-size: 18px; color: #333; margin-bottom: 20px;">
                    🎤 Click "Join Voice Room" to start talking with others!
                </div>

                <div class="voice-controls">
                    <button class="voice-btn" id="joinVoiceBtn" onclick="joinVoiceRoom()">
                        🎤 Join Voice Room
                    </button>
                    <button class="voice-btn disabled" id="talkBtn" onmousedown="startTalking()" onmouseup="stopTalking()">
                        🗣️ Hold to Talk
                    </button>
                    <button class="voice-btn" id="muteBtn" onclick="toggleMute()" style="background: #ff9800; display: none;">
                        🔊 Mute
                    </button>
                    <button class="voice-btn" id="leaveVoiceBtn" onclick="leaveVoiceRoom()" style="background: #f44336; display: none;">
                        📞 Leave Voice
                    </button>
                </div>

                <div class="voice-participants">
                    <h3>👥 Voice Participants (<span id="voiceParticipantCount">0</span>)</h3>
                    <div id="voiceParticipantsList">
                        <div style="color: #666; font-style: italic;">No one in voice yet</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Settings Tab -->
        <div id="settingsTab" class="tab-content">
            <div class="content-header">
                <div class="content-title">
                    ⚙️ Settings
                    <span style="font-size: 12px; color: #666;">Customize your experience</span>
                </div>
            </div>

            <div class="settings-panel">
                <div class="settings-group">
                    <h3>🔔 Notifications</h3>
                    <div class="setting-item">
                        <div>
                            <div>Sound notifications</div>
                            <div style="font-size: 12px; color: #666;">Play sound when receiving messages</div>
                        </div>
                        <div class="setting-toggle" id="soundToggle" onclick="toggleSetting('sound')"></div>
                    </div>
                    <div class="setting-item">
                        <div>
                            <div>Desktop notifications</div>
                            <div style="font-size: 12px; color: #666;">Show notifications even when tab is not active</div>
                        </div>
                        <div class="setting-toggle" id="desktopToggle" onclick="toggleSetting('desktop')"></div>
                    </div>
                </div>

                <div class="settings-group">
                    <h3>🎨 Appearance</h3>
                    <div class="setting-item">
                        <div>
                            <div>Dark mode</div>
                            <div style="font-size: 12px; color: #666;">Switch to dark theme</div>
                        </div>
                        <div class="setting-toggle" id="darkToggle" onclick="toggleSetting('dark')"></div>
                    </div>
                    <div class="setting-item">
                        <div>
                            <div>Compact mode</div>
                            <div style="font-size: 12px; color: #666;">Reduce spacing between messages</div>
                        </div>
                        <div class="setting-toggle" id="compactToggle" onclick="toggleSetting('compact')"></div>
                    </div>
                </div>

                <div class="settings-group">
                    <h3>📊 Data & Storage</h3>
                    <div class="setting-item">
                        <div>
                            <div>Auto-backup</div>
                            <div style="font-size: 12px; color: #666;">Automatically backup messages and settings</div>
                        </div>
                        <div class="setting-toggle active" id="backupToggle" onclick="toggleSetting('backup')"></div>
                    </div>
                    <div class="setting-item">
                        <div>
                            <div>Message persistence</div>
                            <div style="font-size: 12px; color: #666;">Store messages locally and in cloud</div>
                        </div>
                        <div class="setting-toggle active" id="persistToggle" onclick="toggleSetting('persist')"></div>
                    </div>
                </div>

                <div class="settings-group">
                    <h3>🎤 Voice Settings</h3>
                    <div class="setting-item">
                        <div>
                            <div>Voice activity detection</div>
                            <div style="font-size: 12px; color: #666;">Automatically detect when you're speaking</div>
                        </div>
                        <div class="setting-toggle" id="vadToggle" onclick="toggleSetting('vad')"></div>
                    </div>
                    <div class="setting-item">
                        <div>
                            <div>Echo cancellation</div>
                            <div style="font-size: 12px; color: #666;">Reduce echo in voice chat</div>
                        </div>
                        <div class="setting-toggle active" id="echoToggle" onclick="toggleSetting('echo')"></div>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(0,0,0,0.1);">
                    <p style="color: #666; font-size: 14px; margin-bottom: 10px;">ChatHub Pro v2.0</p>
                    <p style="color: #666; font-size: 12px;">Built with ❤️ for seamless communication</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Image Modal -->
<div id="imageModal" class="image-modal" onclick="closeImageModal()">
    <span class="close" onclick="closeImageModal()">&times;</span>
    <img id="modalImage" alt="Full size image">
</div>

<!-- Notification -->
<div id="notification" class="notification"></div>

<script>
    // Application State
    let currentUser = '';
    let messages = [];
    let users = new Set(['You']);
    let settings = {
        sound: false,
        desktop: false,
        dark: false,
        compact: false,
        backup: true,
        persist: true,
        vad: false,
        echo: true
    };

    // Voice Chat State
    let isInVoiceRoom = false;
    let isMuted = false;
    let isTalking = false;

    // GitHub Gist Configuration (for persistence)
    const GITHUB_TOKEN = 'your_github_token_here'; // Set this to your GitHub token
    const MAIN_GIST_ID = 'your_main_gist_id_here'; // For messages and accounts
    const IMAGE_GIST_ID = 'your_image_gist_id_here'; // For images

    // Initialize App
    function initApp() {
        loadSettings();
        applySettings();
        requestNotificationPermission();
        
        // Auto-resize message input
        const messageInput = document.getElementById('messageInput');
        messageInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 100) + 'px';
        });

        // Enter key to send message
        messageInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        // Load persistent data
        loadPersistedData();
    }

    // Authentication
    function login() {
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').
```
