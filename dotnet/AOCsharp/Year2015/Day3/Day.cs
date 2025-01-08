using AOCSolutions;

namespace AOCsharp.Year2015.Day3;

public class Day : IDay
{
    public IPart GetPart(int part)
    {
        return part switch
        {
            1 => new Part1(),
            2 => new Part2(),
            _ => throw new InvalidPartException(part)
        };
    }
}

