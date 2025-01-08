using AOCSolutions;

namespace AOCsharp.Year2015.Day2;

public class Part1 : IPart
{
    public string GetSolution(TextReader input)
    {
        var presents = Parser.ParseInput(input);
        return presents.Sum(present => present.RequiredPaperArea()).ToString();
    }
}
