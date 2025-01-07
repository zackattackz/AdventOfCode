using AOCSolutions;

namespace AOCRunner;

public static class SolutionsParse
{
    public static ISolutions? TryGetSolutions(string input)
    {
        return input switch
        {
            AOCsharp.Solutions.Name => new AOCsharp.Solutions(),
            AOCfsharp.SolutionsName => new AOCfsharp.Solutions(),
            _ => null,
        };
    }
}