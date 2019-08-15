public interface MyList<E> extends java.lang.Iterable<E> {
    public void add(E e);
    
    public void add(int index, E e);
    
    public void clear();
    
    public void contains(E e);
    
    public void get (int index);
    
    public void indexOf(E e);
    
    public void isEmpty();
    
    public int lastIndexOf(E e);
    
    public void remove(E e);
    
    public void remove(int index);
    
    public void Object set(int index, E e);
    
    public void size();
    
}