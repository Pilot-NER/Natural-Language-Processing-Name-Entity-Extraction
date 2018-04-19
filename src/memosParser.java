import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Collections;

public class memosParser {

    public static void main(String[] args) {
        String memosFileName= "Sample memos - memos.csv";
        List<String> memosList = new ArrayList<>();
        List<String> vendorsList = new ArrayList<>();
        String line = "";

        try (BufferedReader br = new BufferedReader(new FileReader(memosFileName))) {
            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] entry = line.split(",");
                memosList.add(line.substring(0, line.lastIndexOf(",")));
                vendorsList.add(entry[entry.length - 1]);

            }
        } catch (IOException e) {
            e.printStackTrace();
        }

//        for (String memo : memosList){
//            System.out.println(memo);
//        }
//
//        for (String vendor : vendorsList) {
//            System.out.println(vendor);
//        }

        try {
            // choose 100 random memos
//            List<String> memosDupList = new ArrayList<>(memosList);
//            Collections.shuffle(memosDupList);
//            memosDupList = new ArrayList<>(memosDupList.subList(0, memosDupList.size()-1));
            String s = String.join("|", memosList);

            BufferedWriter train_data = new BufferedWriter(new FileWriter("MemosText.txt"));
            train_data.write(s);
            train_data.close();
        }
        catch (IOException e){
            System.out.println("Exception");
        }

        // output training and testing dataset
        StringBuilder contentBuilder = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader("MemosText_testFile.tsv")))
        {

            String sCurrentLine;
            while ((sCurrentLine = br.readLine()) != null)
            {
                contentBuilder.append(sCurrentLine).append("\n");
            }
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

        String tokenized_memos = contentBuilder.toString();
        String[] memos_with_tokens = tokenized_memos.split("\\|");
        int memos_size = memos_with_tokens.length;
        List<String> memosL = Arrays.asList(memos_with_tokens);
        Collections.shuffle(memosL);
        Object[] memosShuffledList = memosL.toArray();
//        for (String s:memosShuffledList){
//            System.out.print(s);
//        }


//-------------------------------------------- 10%
        int endIndex = memos_size / 10;
        String trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        String testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train1.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test1.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 20%
        endIndex = memos_size * 2 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train2.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test2.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }
//-------------------------------------------- 30%
        endIndex = memos_size * 3 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train3.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test3.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 40%
        endIndex = memos_size * 4 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train4.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test4.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 50%
        endIndex = memos_size * 5 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train5.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test5.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 60%
        endIndex = memos_size * 6 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train6.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test6.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 70%
        endIndex = memos_size * 7 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train7.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test7.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 80%
        endIndex = memos_size * 8 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train8.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test8.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 90%
        endIndex = memos_size * 9 / 10;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train9.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test9.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

//-------------------------------------------- 100%
        endIndex = memos_size-1;
        trainText = "";
        for (int i = 0; i < endIndex; i++){
            trainText += memosShuffledList[i];
        }

        testText = "";
        for (int i = endIndex; i < memos_size; i++){
            testText += memosShuffledList[i];
        }
//        System.out.println(text);

        try (PrintWriter out = new PrintWriter("train10.tok")) {
            out.println(trainText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }

        try (PrintWriter out = new PrintWriter("test10.tsv")) {
            out.println(testText);
        }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }
    }

}