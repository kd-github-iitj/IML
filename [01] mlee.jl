totalObservations = 50
parameterS = range(1.0, totalObservations, step=0.1)

parameterTheta = range(0.1, 0.9, length=100)
likelihood(S, o) = S * log(o) + (totalObservations - S) * log(1.0 - o)

#install the "plot pachage if not tere
using Plots
gr()

# maximum likelihood Estiation (MLE)
heatmapPlot = Plots.heatmap(parameterS,parameterTheta,(S, o) -> likelihood(S, o), color=:jet, xlabel="S", ylabel="θ", title="Bird's Eye View")

# mle on S = 25

selectedS = 25
vline!([selectedS], label=false, color=:black)

linePlot = Plots.plot(parameterTheta, o -> likelihood(selectedS, o), label=false, xlabel="θ", title="L(θ|S=$selectedS)")

Plots.plot(heatmapPlot, linePlot)
savefig("D:\ML\iml-hands-on-submission-main\my_images")
