import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Shapes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	}
}

class Polygon2D {

	private Point2D[] v;

	public Polygon2D() {  
		v = new Point2D[0];
	}


	public Polygon2D(Point2D[] points) {  
		v = new Point2D[points.length];
		for (int i=0; i<points.length; i++) {
			v[i] = new Point2D(points[i]);
		}
	}

	public Polygon2D(Polygon2D poly) { 
		v = new Point2D[poly.v.length];
		for (int i=0; i<poly.v.length; i++) {
			v[i] = new Point2D(poly.v[i]);
		}
	}

	public void addPoint(Point2D p) {
		v = Arrays.copyOf(v, v.length + 1);
		v[v.length-1] = new Point2D(p);
	}

	public int size() {
		return v.length;
	}

	public Point2D[] asPointsArray() {
		return Arrays.copyOf(v, v.length);
	}

	public void draw() {
		for (int i=0; i<v.length; i++) {
			if (i < v.length-1)
				StdDraw.line(v[i].getX(), v[i].getY(), v[i+1].getX(), v[i+1].getY());
			else
				StdDraw.line(v[i].getX(), v[i].getY(), v[0].getX(), v[0].getY());
		}
	}

	public void drawFilled() {
		double[] X = new double[v.length];
		double[] Y = new double[v.length];
		for (int i=0; i<v.length; i++) {
			X[i] = v[i].getX();
			Y[i] = v[i].getY();
		}
		StdDraw.filledPolygon(X, Y);
	}


}


class Point2D implements Comparable<Point2D>{

	private final double x;
	private final double y;

	public Point2D(double x, double y) { 
		this.x = x;
		this.y = y;
	}

	public Point2D(Point2D p) { 
		if (p == null)  System.out.println("Point2D(): null point!");
		x = p.getX();
		y = p.getY();
	}

	public double getX() { 
		return x; 
	}

	public double getY() { 
		return y; 
	}

	//calculate turning direction, similar to polar angle 
	public static double turningDirection(Point2D p0, Point2D p1, Point2D p2) {
		double a1 = (p1.getX()-p0.getX());
		double a2 = (p2.getX()-p0.getX());
		double b1 = (p1.getY()-p0.getY());
		double b2 = (p2.getY()-p0.getY());
		double z = (a1*b2)-(b1*a2);
		if(z < 0) return 1; //right
		else if(z > 0) return -1; //left
		else //colinear
			return 0;
	}
	public int compareTo(Point2D p2) { //compare two points
		Point2D p1 = this;
		if(p1.getX()+p1.getY()>p2.getX()+p2.getY())
			return -1;
		else if(p1.getX()+p1.getY()<p2.getX()+p2.getY())
			return 1;
		else
			return 0;
	}

	@Override
	public String toString() {
		return ("(" + x + "," + y + ")\n");
	}

	public void draw() {
		StdDraw.point(x, y);
	}

}


class Vector implements Comparable<Vector>{ //2D vector
	private final Point2D p0;
	private final Point2D p1;

	//constructor
	public Vector(Point2D p0, Point2D p1) {
		this.p0 = p0;
		this.p1 = p1;
	}
	//getters
	public Point2D getPoint() { return p1; }

	public Point2D getP0() { return p0; }
	public Point2D getP1() { return p1; }

	//method to remove collinear points
	public static Point2D[] removeColinear(Vector[] v){
		List<Point2D> hullPoints = new ArrayList<Point2D>(); //create hull points
		for (int i=0; i<v.length; i++){
			double area = v[i].calcArea(v[(i+1)%(v.length)]); //calculate area under 3 points
			if(area < 0.0001){ //if less than threshold 
			}
			else{
				hullPoints.add(v[i].getP1()); //add to hull points
			}
		}
		//convert to Point2D array
		Point2D[] hull = new Point2D[hullPoints.size()];
		hull = hullPoints.toArray(hull);
		return hull;
	}

	//method to calculate area for removing collinear points
	public double calcArea(Vector B){
		Vector A = this;
		return A.p0.getX() * (A.p1.getY() - B.p1.getY()) + A.p1.getX() * (B.p1.getY() - A.p0.getY()) + B.p1.getX() * (A.p0.getY() - A.p1.getY());

	}

	//compareto method
	public int compareTo(Vector B){

		Vector A = this;
		if(A == B) return 0;
		double a1 = (A.p1.getX()-A.p0.getX());
		double a2 = (B.p1.getX()-A.p0.getX());
		double b1 = (A.p1.getY()-B.p0.getY());
		double b2 = (B.p1.getY()-B.p0.getY());
		double cross = (a1*b2)-(b1*a2); //cross product

		if(cross == 0) return 0; //collinear
		else if(cross > 0) return 1; 
		else if(cross < 0) return -1;
		return 0;
	}

	@Override
	public String toString() {
		return ("\nEdge Point 1: (" + p0.getX() + "," + p0.getY() + ")" + "\tEdge Point 2: (" + p1.getX() + "," + p1.getY() + ")");
	}

}

class StackNode<T> { //stack for hull points

	private Node<T> head;  //head of stack
	private int size = 0;

	private static class Node<T> {
		T item;
		Node<T> next;
	}

	public void push(T item) { //push item onto stack
		Node<T> newNode = new Node<T>();
		newNode.item = item;
		newNode.next = head;
		head = newNode;
		size++;
	}

	public T pop() { //pop item off of stack
		if (head == null) return null; //stack is empty
		T item = head.item;
		head = head.next;
		size--;
		return item;
	}

	public int size() {	return size; }

	public boolean isEmpty() {
		return (size == 0);
	}

	@Override
	public String toString() {
		String s = "";
		Node<T> tmp = head;
		while (tmp != null) {
			s += tmp.item.toString() + " -> ";
			tmp = tmp.next;
		}
		return s;
	}

	public T peek() { //look at top item in stack
		if (head == null) return null; // stack is empty
		T item = head.item;
		return item;
	}

	public T sneeky_peek() { //look at item 2 places in
		if (head.next == null) return null; // stack is empty
		T item = head.next.item;
		return item;
	}

}


//reference
//http://www.science.smith.edu/~istreinu/Teaching/Courses/274/Spring98/Projects/Philip/fp/visibility.htm
//https://taipanrex.github.io/2016/10/19/Distance-Tables-Part-2-Lees-Visibility-Graph-Algorithm.html
class VisibilityGraph {

	//method to determine if two vectors intersect each other
	public static Boolean lineOfSight(Vector v1, Vector v2){
		//v1.getP1() is one of the points making the v1 vector
		//v1.getP0() is the other
		double denominator = ((v1.getP1().getX()-v1.getP0().getX()) * (v2.getP1().getY()-v2.getP0().getY())) - ((v1.getP1().getY()-v1.getP0().getY()) * (v2.getP1().getX()-v2.getP0().getX())); 
		if (denominator == 0)
		{
			return false;
		}
		double numerator1 = ((v1.getP0().getY()-v2.getP0().getY()) * (v2.getP1().getX()-v2.getP0().getX())) - ((v1.getP0().getX()-v2.getP0().getX()) * (v2.getP1().getY()-v2.getP0().getY()));
		double numerator2 = ((v1.getP0().getY()-v2.getP0().getY()) * (v1.getP1().getX()-v1.getP0().getX())) - ((v1.getP0().getX()-v2.getP0().getX()) * (v1.getP1().getY()-v1.getP0().getY()));
		if (numerator1 == 0 || numerator2 == 0)
		{
			return false;
		} 
		double r = numerator1 / denominator;
		double s = numerator2 / denominator;
		//returns true or false (boolean)
		return (r > 0 && r < 1) && (s > 0 && s < 1); 
	}

	//method to get the edge points of a convex hull
	public static List<Vector> getEdges(Point2D[][] convexHulls){
		List<Vector> edges = new ArrayList<Vector>();
		for(int i=0; i<convexHulls.length;i++){
			int k = 1;
			for(int j=0; j<convexHulls[i].length;j++){
				if(k==convexHulls[i].length){
					k = 0;
				}
				edges.add(new Vector(convexHulls[i][j], convexHulls[i][k]));
				k++;
			}
		}
		//returns a List<Vector>
		return edges;
	}

	//method to calculate the distance between two points
	public static double dist(Point2D p1, Point2D p2){
		//euclidian formula
		double distance = Math.sqrt(Math.pow((p2.getX()-p1.getX()),2)+Math.pow((p2.getY()-p1.getY()),2));
		return distance;
	}

	//method that gets the index of an array at a certain value (works as vertices are unique i.e map/dictionary)
	public static int indexOfArray(Point2D array[], Point2D key) {
		int returnvalue = -1;
		for (int i = 0; i < array.length; ++i) {
			//check key and array value
			if (key == array[i]) {
				returnvalue = i;
				break;
			}
		}
		return returnvalue;
	}

	//method to append two arrays
	public static <T> T[] concat(T[] first, T[] second) {
		T[] result = Arrays.copyOf(first, first.length + second.length);
		System.arraycopy(second, 0, result, first.length, second.length);
		return result;
	}

	//method that generates the paths on the visibility graph
	public static List<Graph.Edge> generatePaths(Point2D[][] convexHulls, Point2D startingPoint, Point2D endPoint){
		List<Vector> edges = getEdges(convexHulls);	//edges of convex hulls (to check for intersections)
		List<Vector> lines = new ArrayList<Vector>(); //temp. Vector list
		List<Graph.Edge> paths = new ArrayList<Graph.Edge>(); //list of paths in graph

		int s = 0; //counters
		int intersections = 0;

		for(int i=0; i<convexHulls.length;i++){ //for each polygon
			for(int j=0; j<convexHulls[i].length;j++){//..for each point in each polygon
				for(int k=0; k<convexHulls.length;k++){ //..connected to each polygon
					for(int l=0; l<convexHulls[k].length;l++){ //..to each point in each polygon
						if(s == 0){
							intersections = 0; //reset intersections to 0
							lines.add(new Vector(startingPoint, convexHulls[k][l])); //add vector from starting point to every other point
							for(int e=0; e<edges.size(); e++){ //for every edge on every convex hull
								if(lineOfSight(lines.get(lines.size()-1),edges.get(e)) == true) //if the line intersects any edge
									intersections++; //increment intersections (could optimise here)
							}
							if(intersections<1){ //if no intersections
								//add to path
								paths.add(new Graph.Edge(startingPoint, lines.get(lines.size()-1).getP1(), dist(startingPoint, lines.get(lines.size()-1).getP1())));
							}
						}
						if(i!=k && s!=0){ //other points (not starting point)
							intersections = 0;
							lines.add(new Vector(convexHulls[i][j], convexHulls[k][l]));
							for(int e=0; e<edges.size(); e++){ 
								if(lineOfSight(lines.get(lines.size()-1),edges.get(e)) == true)
									intersections++;
							}
							if(intersections<1){
								paths.add(new Graph.Edge(lines.get(lines.size()-1).getP0(), lines.get(lines.size()-1).getP1(), dist(lines.get(lines.size()-1).getP0(), lines.get(lines.size()-1).getP1())));
							}
						}
					}
				}
				s++;
			}
		}//end point checks
		for(int i=0; i<convexHulls.length;i++){ 
			for(int j=0; j<convexHulls[i].length;j++){
				intersections = 0;
				lines.add(new Vector(endPoint, convexHulls[i][j]));
				for(int e=0; e<edges.size(); e++){ 
					if(lineOfSight(lines.get(lines.size()-1),edges.get(e)) == true)
						intersections++;
				}
				if(intersections<1){
					paths.add(new Graph.Edge(lines.get(lines.size()-1).getP0(), lines.get(lines.size()-1).getP1(), dist(lines.get(lines.size()-1).getP0(), lines.get(lines.size()-1).getP1())));
				}

			}
		}

		for(int i=0; i<edges.size();i++){
			paths.add(new Graph.Edge(edges.get(i).getP0(), edges.get(i).getP1(), dist(edges.get(i).getP0(), edges.get(i).getP1())));
		}

		return paths; //return list of paths in graph
	}
}
