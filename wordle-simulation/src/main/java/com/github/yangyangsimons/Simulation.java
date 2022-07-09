package com.github.yangyangsimons;

import org.apache.commons.io.IOUtils;

import java.util.Scanner;
import javax.xml.transform.Templates;
import java.io.*;
import java.util.*;

//simon feb 25 2022
public class Simulation {
    public static Scanner scanner = new Scanner(System.in);
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_GREEN = "\u001B[32m";


    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        int tries = 0;
        System.out.println("Wordle: You have five tries");
        String targetWord = GetRandomWord();
        char[] targetChar = new char[5];
        for (int i = 0; i < 5; i++) {
            targetChar[i] = targetWord.charAt(i);
        }
        char[] input = new char[5];
        boolean gameOver = false;

        while (!gameOver) {
            tries++;
            String R1 = scanner.nextLine().toLowerCase();
            if(R1.length() < 5) {
                R1 = scanner.nextLine().toLowerCase();
            }else{
                System.out.println("Five letters only");
            }
            for (int i = 0; i < 5; i++) { //puts the inputWord into a char[]
                answer[i] = answerChoosen.charAt(i);
                input[i] = R1.charAt(i);
            }
            if (PrintWordWithColor(input, answer)) done = true;
        }

        System.out.println("Hey, You Found The Answer in " + ((System.currentTimeMillis() - startTime) / 1000) + " seconds and " + tries + " tries.");
    }

    public static boolean PrintWordWithColor(char[] inputWord, char[] correctWord) {
        boolean correct = true;
        char[] answerTemp = correctWord;
        int[] colorForLetter = new int[5]; //0 is grey, yellow is 1, green is 2

        for (int i = 0; i < 5; i++) { //check for any correct position+letter (green)
            if (inputWord[i] == answerTemp[i]) {
                answerTemp[i] = '-';
                colorForLetter[i] = 2;
            } else correct = false;
        }

        for (int j = 0; j < 5; j++) { //check for any correct letter (yellow)
            for (int k = 0; k < 5; k++) {
                if (inputWord[j] == answerTemp[k] && colorForLetter[j] != 2) {
                    //if that letter is not already green and matches some other letter
                    colorForLetter[j] = 1;
                    answerTemp[k] = '-';
                }
            }
        }

        for (int m = 0; m < 5; m++) {
            if (colorForLetter[m] == 0) System.out.print(inputWord[m]);
            if (colorForLetter[m] == 1) System.out.print(ANSI_YELLOW + inputWord[m] + ANSI_RESET);
            if (colorForLetter[m] == 2) System.out.print(ANSI_GREEN + inputWord[m] + ANSI_RESET);
        }
        System.out.println("");
        return correct;
    }

    public static String GetRandomWord() {

        List<String> answerList = null;
        try {
            answerList = IOUtils.readLines(new FileReader(new File("/Users/lynnyang/work/wordle/data/allowed_words.txt")));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        //returns a random word from this large list
        int index = (int)(Math.random() * (answerList.size() - 1));
        return answerList.get(index);
    }
}
