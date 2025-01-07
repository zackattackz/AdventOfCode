namespace AOCSolutions;

public interface IDay
{
    public IPart GetPart(int part);
}

public class InvalidPartException(int part) : Exception(_getExceptionString(part))
{
    private static string _getExceptionString(int part) => $"Invalid part: {part}";
}
