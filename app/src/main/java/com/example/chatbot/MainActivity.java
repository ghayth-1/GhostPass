package com.example.chatbot;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText edtName;
    private Button btnStart;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        edtName = findViewById(R.id.edtName);
        btnStart = findViewById(R.id.btnStart);

        btnStart.setOnClickListener(v -> {
            String name = edtName.getText().toString().trim();
            Intent i = new Intent(this, ChatActivity.class);
            i.putExtra("username", name);
            startActivity(i);
        });
    }
}
