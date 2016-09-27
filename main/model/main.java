package model;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

import static com.sun.tools.doclint.Entity.image;

/**
 * Created by courtney on 2016-09-26.
 */
public class testHash {
    // initializes engToBliss hashmap
    Map engToBliss = new HashMap();

    // create key-val dictionary pairs for English & Bliss words, like so:
    engToBliss.put("dog", "bliss_dog.jpg");
    engToBliss.put("rain", "bliss_rain.png");
    // except actual .PNG/.JPG/etc. files as values

    public void insert(String engWord, Image blissImg) {
        // Adds given English word and corresponding
        // Blissymbol as key-val pair to engToBliss.
        engToBliss.put(engWord, blissImg);
    }
}
