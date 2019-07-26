public class MyPoint {
    
    private double x;
    private double y;
    
    MyPoint (){
        this.x = 0;
        this.y = 0;
    }

    MyPoint(double x, double y){
        this.x = x;
        this.y = y;
    }
    
    public double getX(){
        return this.x;
    }
    
    public double getY(){
        return this.y;
    }
    
    public double distance(MyPoint point){
        return Math.sqrt(point.getX()*point.getX() + 
                         point.getY()*point.getX()) - 
                         Math.sqrt(this.x*this.x + this.y*this.y);
    }
    
    public double distance(double x, double y){
       
        return Math.sqrt(this.x*this.x + this.y*this.y) - 
            Math.sqrt(x*x + y*y);
    }
}