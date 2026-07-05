import java.util.Arrays;
public class mean {
    private int[] dataSet;

    // Constructor
    public mean(int[] dataSet){
        this.dataSet = dataSet;
    }

    public double calculateMean(){
        if (dataSet == null || dataSet.length == 0) return 0;
        double sumOfelements = 0.0;
        for(int i : dataSet){
            sumOfelements += i;
        }
        return sumOfelements/dataSet.length;
    }
    public String toString(){
        return Arrays.toString(dataSet);
    }

    public static void main(String[] args){
        int[] myArray = {45,56,78,89,56,12};

        // Object creation
        mean me = new mean(myArray);
        System.out.print("The mean of your data set = "+ me.calculateMean());
    }
}


