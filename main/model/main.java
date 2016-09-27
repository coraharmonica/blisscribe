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

    // TODO: create key-val dictionary pairs for English & Bliss words, like so:
    engToBliss.put("dog", "blissymbol-dog.jpg");
    engToBliss.put("rain", "bliss_rain.png");
    // except actual .PNG/.JPG/etc. files as values.

    // What would be the best way to create the dictionary? Write a method to compile an
    // English-to-Bliss dictionary from input file?

    public void insert(String engWord, Image blissImg) {
        // Adds English word engWord and Blissymbol blissImg as key-val pair to engToBliss.
        //
        // N.B. For now, a key will only be a string and a value will only be an image;
        // in the future however both may need to be lists (of strings and of images) to
        // allow for single words/symbols with multiple meanings.
        engToBliss.put(engWord, blissImg);
    }
}