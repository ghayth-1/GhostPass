package com.example.chatbot;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.ImageButton;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

public class ChatFragment extends Fragment {

    private RecyclerView recyclerView;
    private MessageAdapter adapter;
    private EditText edtMessage;
    private ImageButton btnSend;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_chat, container, false);

        recyclerView = v.findViewById(R.id.recyclerChat);
        edtMessage = v.findViewById(R.id.edtMessage);
        btnSend = v.findViewById(R.id.btnSend);

        adapter = new MessageAdapter(ChatRepository.getInstance().getMessages());
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        recyclerView.setAdapter(adapter);

        btnSend.setOnClickListener(view -> sendMessage());

        return v;
    }

    private void sendMessage() {
        String text = edtMessage.getText().toString().trim();
        if (text.isEmpty()) return;

        ChatRepository repo = ChatRepository.getInstance();
        repo.addMessage(new Message(text, true));

        String reply = botReply(text);
        repo.addMessage(new Message(reply, false));

        int size = repo.getMessages().size();
        adapter.notifyItemRangeInserted(size - 2, 2);
        recyclerView.scrollToPosition(size - 1);
        edtMessage.setText("");

        ChatStorage.save(requireContext(), repo.getMessages());
    }

    private String botReply(String userText) {
        String t = userText.toLowerCase();
        if (t.contains("bonjour")) return "Bonjour !";
        if (t.contains("merci")) return "Avec plaisir.";
        if (t.contains("au revoir")) return "À bientôt !";
        return "Je suis un bot local :)";
    }
}
