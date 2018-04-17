import java.io.*;
import java.util.ArrayList;
import java.util.List;
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
            List<String> memosDupList = new ArrayList<>(memosList);
            Collections.shuffle(memosDupList);
            memosDupList = new ArrayList<>(memosDupList.subList(0, memosDupList.size()-1));
            String s = String.join("|", memosDupList);

            BufferedWriter train_data = new BufferedWriter(new FileWriter("test.txt"));
            train_data.write(s);
            train_data.close();
        }
        catch (IOException e){
            System.out.println("Exception");
        }

    }

}