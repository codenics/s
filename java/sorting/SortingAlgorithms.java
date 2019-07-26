import java.util.Stack;
public class SortingAlgorithms {
  /**
  Method takes an array of integers and returns
  array of integers;
  **/
  public int[] insertionSort (int [] list){

/**
Loop over the entire list and
perform sorting along the line
**/
int i, j, temp, currentElement;
    for (i = 1; i<list.length; i++){
      currentElement = list[i];
      j = i-1;

      /**
        while the j is not negative and the currentElement
        element in the list is greater the value on its left;
        swap it.
      **/
      while(j >= 0 && currentElement < list[j]){
        temp = list[j];
        list[j] = list[j+1];
        list[j+1] = temp;
        j--;
      }
    }
    return list;
  }


  public String reverseString (String s){
    StringBuilder sb = new StringBuilder();
    for (int i = s.length() - 1; i >= 0; i--) {
      sb.append(s.charAt(i));

    }
    return sb.toString();

  }
  public String NumOfVowelsAndConst (String str ){
    str = str.trim();
    str = str.toLowerCase();

    String s = new String();
    String [] ss = str.split(" ");
    for(int i = 0; i<ss.length; i++){
      s+=ss[i];
    }
    int count = 0;
    s = s.trim();
    s = s.toLowerCase();

    for (int i = 0; i < s.length(); i++){
      if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'o'
      || s.charAt(i) == 'i' || s.charAt(i) == 'u' || s.charAt(i) == 'y'){
        count++;
      }
    }
    int consonants = s.length() - count;
    return "There are " + count + " vowels and " + consonants + " consonants.";
   }

   public String reverseStringWithStack (String str){
     Stack strStack = new Stack();
     StringBuilder sb = new StringBuilder();

     for (int i = 0; i<str.length(); i++) {
       strStack.push(str.charAt(i));
     }
     for (int i = 0; i< str.length(); i++){
       sb.append(strStack.pop());
     }
     return sb.toString();
   }

}
