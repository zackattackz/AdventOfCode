using AOCSolutions;

namespace AOCsharp.Year2015.Day2;

public class Part2 : IPart
{
    public string GetSolution(TextReader input)
    {
        var presents = Parser.ParseInput(input);
        return presents.Sum(present => present.RequiredRibbonLength()).ToString();
    }
}
