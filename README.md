# End Semester Examination, Set 1, Question 2
# Correct the Campus Task List Default View

**Total: 30 marks | Submit one PDF**

## Problem

Campus organisers need the default task view to show unfinished work. The current program shows completed tasks too. Repair the default view without removing records or breaking the explicit all view.

Starter: https://github.com/kalviumcommunity/endsem-campus-task-view

Use your assigned repository. Run supplied Python files from project root using your available Python 3 launcher. Files are small and use the standard library. README.md documents the entry point and existing checks. Do not change README.md, app.py, sample_data.py or checks.py.

## Requirements

- Calling titles_for_view(tasks) with no mode must return only unfinished titles in original order.
- Explicit mode "unfinished" must do the same.
- Explicit mode "all" must return all titles in original order.
- Empty input and an unfinished view of completed-only input return an empty list.
- Do not alter input records, their values or their order. Priority must not affect unfinished selection.
- Only supplied modes and record structure are in scope. No new interface or dependency is needed.

Editable files: task_view.py, regression_check.py and RUNBOOK.md. Inspect other files as needed. Keep existing checks and supplied non-placeholder regression assertions unchanged.

## Task 1: Reproduce and trace

Inspect project files and initial Git status. Run app.py. Record expected versus observed default and all results for the supplied mixed data. Use code search or editor navigation to locate the public view function and selection helper. Explain the path from sample input to displayed titles and identify their source files.

Evidence: initial status/files, actual run, expected/observed comparison and located caller/helper with short trace explanation.

## Task 2: Expose the coverage gap

Create a repair branch before making changes. Run checks.py unchanged. In regression_check.py, complete only the two marked expected-value placeholders using the requirements and supplied data. Execute the regression against unchanged faulty task_view.py, capturing failure before repair. Explain why the old checks passing does not establish correct default behaviour.

Evidence: branch, original check result, completed regression assertions, pre-fix failure, unchanged implementation at this point and coverage-gap explanation.

## Task 3: Repair and validate

Make a focused correction in task_view.py. Remove any temporary diagnostics. Rerun app.py, existing checks and the complete regression. Verify default and explicit unfinished views, explicit all, completed-only, low-priority unfinished, empty input, original order and unchanged input records using the supplied checks. Keep expectations derived from requirements, not from incorrect output. Explain the cause and correction briefly.

Evidence: focused diff, corrected actual output, complete successful check results and cause/correction explanation. No hard-coded sample outputs, deleted input data or weakened assertions.

## Task 4: Document and propose

Complete RUNBOOK.md with actual reproduction, cause, change, run/check commands, observed results and one testing limit. Review staged changes, make a meaningful commit and push repair branch. Open PR into main in the same assigned repository. Include problem, cause, change and actual validation in its description. Show open state and branch direction, plus final clean local working tree. Leave PR open for review.

Evidence: completed runbook, staged review, commit/push, open PR with requested description/direction and clean state. No merge required.

## Submission

Submit one PDF with four task sections, readable labelled screenshots and requested short answers. Capture intermediate states before continuing. Multiple screenshots per task allowed. Do not include credentials.
