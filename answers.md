# Short Answer (Reasoning)

**1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?**  
I would use **data augmentation** (e.g., paraphrasing, synonym replacement) to expand the dataset and apply **transfer learning** by fine-tuning a pre-trained language model like DistilBERT. Additionally, **active learning** could help by labeling the most informative examples first.

**2. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?**  
I would curate a **balanced and diverse training dataset**, monitor model predictions for biased patterns, and implement **content filters or post-processing rules**. Regular audits and human-in-the-loop checks can help catch unsafe or unexpected outputs.

**3. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?**  
I would provide **clear context and constraints** in the prompt (e.g., recipient industry, name, role, or recent activity) and ask the model to produce **short, varied, and specific openers**. Including examples of good openers and explicitly instructing the model to avoid generic phrases improves relevance.
