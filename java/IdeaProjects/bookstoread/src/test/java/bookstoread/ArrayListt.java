package bookstoread;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayListt {
    private List<String> stringList;

    @BeforeEach
    void init(){
        stringList = new ArrayList<>();
    }
    @Test
    public void empArrayList(){
        assertTrue(stringList.isEmpty(), "ArrayList must be empty.");
    }
    @Test
    public void oneElementInList(){
        stringList.add("Assembly");
        assertEquals(1, stringList.size());
    }

    public static class BookShelfSpec {

        private Bookshelf bookshelf;

        //Replace the declare and initialisation of BookShelf Class in every Test Method
        @BeforeEach
        void init (){
            bookshelf = new Bookshelf();
        }

        @Test
        public void ShelfEmptyWhenNoBookAdded() throws Exception{
          //  Bookshelf bookshelf = new Bookshelf();
            List<String> books = bookshelf.getBooks();

            assertTrue(books.isEmpty(), "BookShelf should be empty.");
        }
        @Test
        void bookShelfContainsTwoBooksWhenTwoBooksAdded(){
           // Bookshelf bookshelf = new Bookshelf();
            bookshelf.add("Effective Java", "Code Complete");

            List<String> books = bookshelf.getBooks();
            assertEquals(2, books.size(), "BookShelf Should have 2 books");
        }

        @Test
        public void emptyBookShelfWhenAddedIsCalledWithoutBooks(){
            //Bookshelf bookshelf = new Bookshelf();
            bookshelf.add();

            List<String> books = bookshelf.getBooks();
            assertTrue(books.isEmpty(), "BookShelf should be empty.");
        }
        @Test
        void booksReturnedFromBookShelfIsImmutableForClient(){
            //Bookshelf bookshelf = new Bookshelf();

            bookshelf.add("Effective Java", "Code Complete");
            List<String> books = bookshelf.getBooks();

            try {
                books.add("Mystical Month");
                fail("should not be able to add books");
            }catch (Exception e){
                assertTrue(e instanceof UnsupportedOperationException, "Should throw UnsupportedOperationException");
            }
        }

        @Disabled
        @Test
        void bookShelfArrangeByBookTile(){
            bookshelf.add("Effective Java", "Code Complete", "The Mystical Man-Month");
            List<String> books  = bookshelf.arrange();
            assertEquals(Arrays.asList("Code Complete", "Effective Java", "The Mystical Man-Month"), books,
                    "Books in a bookshelf should be arranged lexicographically by book title ");
        }
    }
}
