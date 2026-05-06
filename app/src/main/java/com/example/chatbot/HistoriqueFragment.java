package com.example.chatbot;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

public class HistoriqueFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_historique, container, false);

        RecyclerView rv = v.findViewById(R.id.recyclerHistorique);
        rv.setLayoutManager(new LinearLayoutManager(getContext()));
        rv.setAdapter(new MessageAdapter(ChatRepository.getInstance().getMessages()));

        return v;
    }
}
