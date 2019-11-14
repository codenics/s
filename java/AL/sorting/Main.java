public class Main {
  public static void main(String[] args) {

    int [] list = {2, 3, 4, 4, 8, 6, 1, 4, 0, 5, 5};
    SortingAlgorithms sort = new SortingAlgorithms();

    int [] insertionSorted = sort.insertionSort(list);
    for (int i = 0; i<insertionSorted.length; i++){
      System.out.print(" " + list[i]);
    }
    System.out.println("");

    System.out.println(sort.reverseString("Palindrone"));
    System.out.println(sort.NumOfVowelsAndConst("HellO"));
    System.out.println(sort.NumOfVowelsAndConst("There is a quiet Mouse"));
    System.out.println();
    System.out.println(sort.reverseStringWithStack("Palindrone"));

  }


}
