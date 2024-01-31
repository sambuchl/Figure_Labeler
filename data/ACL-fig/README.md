---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- machine-generated
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: ACL-Fig
size_categories:
- 1K<n<10K
source_datasets:
- original
tags: []
task_categories:
- image-classification
task_ids:
- multi-label-image-classification     
---

# Dataset Card for ACLFig Dataset

<!-- ## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions) -->

## Dataset Description

- **Paper:**
- **Leaderboard:**

### Dataset Summary

1758 total labelled images

The scientific figures dataset contains 1758 scientific figures extracted from 890 research papers(ACL). The scientific figures are in png format.

The dataset has been classified into 19 categories. These are 
-  Algorithms 
- Architecture/Pipeline diagrams
- Bar charts 
- Box Plots 
- Confusion Matrix
- Graph 
- Line Chart 
- Maps 
- Natural Images 
- Neural Networks 
- NLP rules/grammar 
- Pie chart 
- Scatter Plot 
- Screenshots
- Tables
- Trees 
- Pareto chart 
- Venn Diagram 
- Word Cloud


The scientific figures are in the `png` directory.

The `metadata` directory contains metadata extracted from the pdf along with scientific figures in json format.

Finally, the `scientific_figures.csv` file contains following columns/fields:

1. `sci_fig` : Scientific figure name

2. `caption`: Caption text

3. `inline_reference`: Scientific figure contexts mentioned in the research paper

4. `metadata`: metadata json filename

5. `label`: One of the 19 categories as described above.

6. `acl_paper_id`: Unique identifier assigned to each pdf by ACL
### Supported Tasks and Leaderboards

Multi-label classification

## Dataset Creation
The dataset was created using papers in ACL Anthology. 

### Annotations

#### Annotation process
~2k images manually labelled

### Citation Information
TODO

### Contributions

Thanks to [@zebaKarishma](https://github.com/zebaKarishma), [@shauryr](https://github.com/shauryr) and [@KavyaPuranik](https://github.com/KavyaPuranik) for adding this dataset.
