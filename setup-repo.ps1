
$ErrorActionPreference = "Stop"

# Project timeline
$startDate = [datetime]::new(2026, 8, 4)

# 10 phases, 10 days each
$phases = @(
    @{
        Name = "01-python-foundations"
        Topics = @(
            "python-revision", "variables-data-types", "operators",
            "conditionals", "loops", "functions", "lists-tuples",
            "dictionaries-sets", "file-handling", "oop"
        )
    },
    @{
        Name = "02-mathematics-for-ml"
        Topics = @(
            "linear-algebra", "vectors", "matrices",
            "matrix-operations", "statistics", "mean-median-mode",
            "variance-standard-deviation", "probability",
            "distributions", "correlation"
        )
    },
    @{
        Name = "03-python-for-data-science"
        Topics = @(
            "numpy-basics", "numpy-arrays", "numpy-indexing",
            "numpy-mathematics", "pandas-basics", "dataframes",
            "data-cleaning", "missing-values",
            "data-transformation", "data-aggregation"
        )
    },
    @{
        Name = "04-data-visualization"
        Topics = @(
            "matplotlib", "line-charts", "bar-charts",
            "histograms", "scatter-plots", "seaborn",
            "correlation-heatmaps", "box-plots",
            "exploratory-data-analysis", "eda-mini-project"
        )
    },
    @{
        Name = "05-machine-learning-fundamentals"
        Topics = @(
            "what-is-machine-learning", "ml-workflow",
            "supervised-learning", "unsupervised-learning",
            "train-test-split", "feature-engineering",
            "feature-scaling", "encoding", "cross-validation",
            "overfitting-underfitting"
        )
    },
    @{
        Name = "06-supervised-machine-learning"
        Topics = @(
            "linear-regression", "multiple-regression",
            "polynomial-regression", "logistic-regression",
            "knn", "decision-trees", "random-forest",
            "naive-bayes", "svm", "model-comparison"
        )
    },
    @{
        Name = "07-unsupervised-machine-learning"
        Topics = @(
            "kmeans", "hierarchical-clustering", "dbscan",
            "pca", "dimensionality-reduction",
            "anomaly-detection", "association-rules",
            "clustering-evaluation", "unsupervised-eda",
            "clustering-project"
        )
    },
    @{
        Name = "08-model-evaluation-and-optimization"
        Topics = @(
            "confusion-matrix", "accuracy-precision-recall",
            "f1-score", "roc-auc", "regression-metrics",
            "hyperparameter-tuning", "grid-search",
            "random-search", "pipelines", "model-optimization"
        )
    },
    @{
        Name = "09-deep-learning-and-neural-networks"
        Topics = @(
            "neural-network-fundamentals", "perceptron",
            "activation-functions", "forward-propagation",
            "backpropagation", "gradient-descent",
            "tensorflow-pytorch", "build-neural-network",
            "introduction-to-cnn", "deep-learning-experiment"
        )
    },
    @{
        Name = "10-final-projects"
        Topics = @(
            "project-selection", "dataset-collection",
            "data-preprocessing", "eda", "model-development",
            "model-training", "model-evaluation",
            "model-improvement", "documentation", "final-project"
        )
    }
)

$day = 1

foreach ($phase in $phases) {

    New-Item -ItemType Directory -Force `
        -Path $phase.Name | Out-Null

    foreach ($topic in $phase.Topics) {

        $date = $startDate.AddDays($day - 1)
        $dateText = $date.ToString("yyyy-MM-dd")
        $dayText = "{0:D3}" -f $day

        $folderName = "day-$dayText" +
                      "_$dateText" +
                      "_$topic"

        $path = Join-Path $phase.Name $folderName

        New-Item -ItemType Directory -Force `
            -Path $path | Out-Null

        # Daily README
        $readme = @"
# Day $dayText - $topic

**Scheduled Date:** $dateText
**Status:** Not Started

## Learning Objective

Understand and implement $topic.

## Concepts Covered

- Add concepts here.

## Practical Implementation

See solution.py and notebook.ipynb.

## Key Learnings

Document your understanding.

## Resources

Add documentation and learning links.

## Results

Add actual outputs and observations.

## Completion Checklist

- [ ] Theory completed
- [ ] Implementation completed
- [ ] Testing completed
- [ ] Documentation completed
"@

        Set-Content "$path/README.md" $readme -Encoding utf8

        # Python implementation
        $pythonCode = @"
"""
Day $dayText - $topic
Scheduled Date: $dateText
"""

def main():
    print("Day $dayText - $topic")
    print("Start implementing your learning here.")

if __name__ == "__main__":
    main()
"@

        Set-Content "$path/solution.py" $pythonCode -Encoding utf8

        # Notes
        $notes = @"
# Learning Notes - Day $dayText

Date: $dateText

## What I learned

## Important concepts

## Implementation observations

## Errors and solutions

## Further exploration
"@

        Set-Content "$path/notes.md" $notes -Encoding utf8

        # Jupyter notebook starter
        $notebook = @'
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Learning Notebook\n",
        "## Objective\n",
        "Document the concepts and experiments for this day."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "print(\"Start your experiment here!\")"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
'@

        Set-Content "$path/notebook.ipynb" $notebook -Encoding utf8

        $day++
    }
}

Write-Host ""
Write-Host "======================================"
Write-Host "100-DAY REPOSITORY CREATED!"
Write-Host "Total days: $($day - 1)"
Write-Host "Start: 2026-08-04"
Write-Host "End: 2026-11-11"
Write-Host "======================================"
