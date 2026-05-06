package com.example.chatbot;

import android.content.Context;
import android.content.SharedPreferences;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class ChatStorage {
    private static final String PREFS = "chat_prefs";
    private static final String KEY = "history";

    public static void save(Context c, List<Message> list) {
        SharedPreferences sp = c.getSharedPreferences(PREFS, Context.MODE_PRIVATE);
        String json = new Gson().toJson(list);
        sp.edit().putString(KEY, json).apply();
    }

    public static List<Message> load(Context c) {
        SharedPreferences sp = c.getSharedPreferences(PREFS, Context.MODE_PRIVATE);
        String json = sp.getString(KEY, null);
        if (json == null) return new ArrayList<>();
        Type type = new TypeToken<List<Message>>() {}.getType();
        return new Gson().fromJson(json, type);
    }
}
