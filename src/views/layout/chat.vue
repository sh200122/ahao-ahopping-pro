<template>
  <div class="chat-container">
    <header>
      <h1>贾维斯</h1>
    </header>
    <div class="chatbox" ref="chatbox">
      <div
        v-for="(message, index) in messages"
        :key="index"
        :class="['message', message.sender === 'user' ? 'user-message' : 'bot-message']"
      >
        <img
          v-if="message.sender === 'user'"
          src="@/assets/托尼.jpg"
          alt="User Avatar"
          class="avatar user-avatar"
        />
        <img
          v-if="message.sender === 'bot'"
          src="@/assets/贾维斯.jpg"
          alt="Bot Avatar"
          class="avatar bot-avatar"
        />
        <div class="text">{{ message.text }}</div>
      </div>
    </div>
    <div class="input-container">
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="输入消息..." />
      <button @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ChatComponent',
  data () {
    return {
      userInput: '',
      messages: []
    }
  },
  methods: {
    async sendMessage () {
      if (this.userInput.trim() === '') return

      const userMessage = {
        text: this.userInput,
        sender: 'user'
      }

      this.messages.push(userMessage)
      this.userInput = ''

      try {
        const response = await axios.post('http://localhost:5005/webhooks/rest/webhook', {
          sender: 'user',
          message: userMessage.text
        })

        response.data.forEach(botMessage => {
          this.messages.push({
            text: botMessage.text,
            sender: 'bot'
          })
        })

        this.$nextTick(() => {
          this.$refs.chatbox.scrollTop = this.$refs.chatbox.scrollHeight
        })
      } catch (error) {
        console.error('Error sending message to Rasa:', error)
      }
    }
  }
}
</script>

<style scoped>
.chat-container {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  padding: 10px;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  height: 93vh;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

.chatbox {
  flex: 1;
  overflow-y: scroll;
  padding: 10px;
  background-color: #fff;
  border-radius: 10px;
  margin-bottom: 10px;
}

.input-container {
  display: flex;
  gap: 10px;
}

input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  border: none;
  background-color: #a9a9a9;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #5e5e5e;
}

.message {
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.user-message {
  float: right;
  justify-content: flex-end;
  flex-direction: row-reverse;
}

.bot-message {
  float: left;
  justify-content: flex-start;
  flex-direction: row;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin: 0 10px;
  object-fit: cover;
}

.text {
  max-width: 70%;
  padding: 10px;
  border-radius: 10px;
  word-wrap: break-word;
}

.user-message .text {
  background-color: #9fe8a0;
  color: #000;
  border-top-right-radius: 0;
}

.bot-message .text {
  background-color: #e5e5ea;
  color: #000;
  border-top-left-radius: 0;
}
</style>
