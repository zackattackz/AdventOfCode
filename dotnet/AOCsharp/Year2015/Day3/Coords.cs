using AOCSolutions;

namespace AOCsharp.Year2015.Day3;

public static class Coords
{
    public static (int,int) DirCharToCoord(char dirChar)
    {
        return dirChar switch
        {
            '<' => (0,-1),
            '^' => (-1,0),
            '>' => (0,1),
            'v' => (1,0),
            _ => throw new InvalidCoordException(dirChar),
        };
    }

    public static IEnumerable<(int,int)> Parse(TextReader input)
    {
        return input.ReadToEnd().Trim().Select(DirCharToCoord);
    }
}

public class InvalidCoordException (char dirChar) : Exception(_getExceptionString(dirChar))
{
    private static string _getExceptionString(int dirChar) => $"Invalid direction character: {dirChar}";
}

