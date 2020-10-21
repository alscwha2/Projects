package edu.yc.oats.algs;

public class Rational
{
	private long numerator;
	private long denominator;

	public Rational (long numerator, long denominator)
	{
		if (denominator == 0) throw new IllegalArgumentException("A rational number cannot haver 0 in the denominator");
		this.numerator = numerator;
		this.denominator = denominator;
		if (numerator != 0) this.simplify();
	}

	private void simplify()
	{
		for (long i = gcd(this.numerator, this.denominator); i != 0 && i != 1; i = gcd(this.numerator, this.denominator)) {
			this.numerator /= i;
			this.denominator /= i;
		}
	}

	private long gcd(long p, long q)
	{
		if (q == 0) return p;
		long r = p % q;
		return gcd(q, r);
	}

	public long numberator()
	{
		return this.numerator;
	}

	public long denominator()
	{
		return this.denominator;
	}

	public Rational plus(Rational b)
	{
		long unsimpNumerator = this.numerator * b.denominator + this.denominator * b.numerator;
		long unsimpDenominator = this.denominator * b.denominator;
		return new Rational(unsimpNumerator, unsimpDenominator);
	}

	public Rational minus(Rational b)
	{
		return plus(new Rational(b.numerator * -1, b.denominator));
	}

	public Rational times(Rational b)
	{
		return new Rational(this.numerator * b.numerator, this.denominator * b.denominator);
	}
	public Rational divides(Rational b)
	{
		if (b.numerator == 0) throw new IllegalArgumentException("Division by 0 is undefined.");
		return times(new Rational(b.denominator, b.numerator));
	}

	public boolean equals(Rational that)
	{
		return this.numerator == that.numerator && this.denominator == that.denominator;
	}

	public String toString()
	{
		return this.numerator + "/" + this.denominator;
	}

	public static void main(String[] args) {
		long n = Long.parseLong(args[0]);
		long d = Long.parseLong(args[1]);
		Rational r = new Rational(n, d);
		long n2 = Long.parseLong(args[2]);
		long d2 = Long.parseLong(args[3]);
		Rational r2 = new Rational(n2, d2);
		System.out.println(r + " plus " + r2 + " = " + r.plus(r2));
		System.out.println(r + " minus " + r2 + " = " + r.minus(r2));
		System.out.println(r + " times " + r2 + " = " + r.times(r2));
		System.out.println(r + " divides " + r2 + " = " + r.divides(r2));
		System.out.println(r + " equals " + r2 + " = " + r.equals(r2));
		System.out.println(r.numberator() + " " + r.denominator());
	}
}