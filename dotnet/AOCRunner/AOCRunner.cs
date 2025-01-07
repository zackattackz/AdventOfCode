namespace AOCRunner;

internal class AOCRunner
{
    private const string BadInputExitMessage = "Usage: runner csharp|fsharp <YEAR> <DAY> <PART>";
    private const int BadInputExitCode = 1;

    private static void _exit(string message, int code)
    {
        Console.WriteLine(message);
        Environment.Exit(code);
    }
    public static void Main(string[] args)
    {
        if (args.Length != 4)
        {
            _exit(BadInputExitMessage, BadInputExitCode);
            return;
        }

        var solutions = SolutionsParse.TryGetSolutions(args[0]);

        if (solutions is null ||
            !int.TryParse(args[1], out var year) ||
            !int.TryParse(args[2], out var day) ||
            !int.TryParse(args[3], out var part))
        {
            _exit(BadInputExitMessage, BadInputExitCode);
            return;
        }

        using var inputReader = InputReader.Get(year, day);
        Console.WriteLine(solutions.Solve(year, day, part, inputReader));
    }
}
