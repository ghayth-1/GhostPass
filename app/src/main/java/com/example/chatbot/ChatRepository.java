package com.example.chatbot;

import java.util.ArrayList;
import java.util.List;

public class ChatRepository {
    private static ChatRepository instance;
    private final List<Message> messages = new ArrayList<>();

    private ChatRepository() {}

    public static synchronized ChatRepository getInstance() {
        if (instance == null) instance = new ChatRepository();
        return instance;
    }

    public List<Message> getMessages() {
        return messages;
    }

    public void addMessage(Message m) {
        messages.add(m);
    }
}
