package bookstoread;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;


public class Bookshelf {

    private final List<String> books = new ArrayList<String>();

    public List<String> getBooks(){
        //return books;
        //Changed to return unmodifiable List.
        return Collections.unmodifiableList(books);
    }

    public void add(String ... bookToAdd){
        for (String book : bookToAdd) {
            books.add(book);
        }
    }
    public List<String> arrange(){
         books.sort(Comparator.naturalOrder());
         return books;
    }


}
