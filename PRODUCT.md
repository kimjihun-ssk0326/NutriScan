# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Delegated: React + Vite (TypeScript), built as static files and hosted on S3 + CloudFront. The backend is Python on AWS (the repo's `.gitignore` is Python's), called over HTTP. A static SPA fits the AWS hosting the README commits to and needs no Node server. Mobile web is the main target, so the photo flow must work through a phone browser's camera/file input.

## Users

Everyday self-trackers in Korea. They want to know what is in a meal they are about to eat, or just ate, without the work of a food diary. They usually have a phone in one hand at the table.

## Product Purpose

NutriScan turns one food photo into a nutrition breakdown: which foods are on the plate and how much energy and how many nutrients they carry. It exists because manual logging (searching a database, guessing portions) is tedious enough that most people give it up. It succeeds when logging a meal takes about as long as taking the photo, and people keep doing it.

## Positioning

- **Photo only, no typing.** One photo gives the full result. Typing in a search box is a fallback, not the main path.
- **Built for Korean food.** It recognizes Korean dishes, banchan and shared table meals that Western-trained calorie apps misidentify or can't split into dishes.

## Operating Context

- Used on a phone at mealtime, often one-handed, in restaurants and at home.
- Korean meals often share several dishes across the table, so the portion one person eats is ambiguous.
- The core loop: take or upload a photo → see the recognized foods and nutrition → save the meal to the log.

## Capabilities and Constraints

In scope now:
- Single-photo analysis: upload or take a photo, see the recognized foods and their nutrition.
- Meal log and history: save analyzed meals and review daily and weekly totals.

Out of scope for now: accounts/login, goals and daily targets.

Open decisions:
- Which recognition model or AWS AI service to use, and which nutrition data source.
- How users correct a wrong recognition or a wrong portion.
- Where the meal log is stored while there are no accounts (on the device or server-side).

## Brand Commitments

- Name: NutriScan.
- UI language: Korean first. English may come later, so copy should not be hardcoded in a way that blocks translation.

## Evidence on Hand

None yet. There are no users, accuracy benchmarks, testimonials or sample data. Do not invent accuracy figures, user counts or reviews.

## Product Principles

1. **The photo is the input.** Every extra tap or field between the shutter and the result has to justify itself.
2. **Korean meals are the default case,** not an edge case: multiple dishes, shared plates, banchan.
3. **Say how sure it is.** Recognition will sometimes be wrong. Show the result plainly and make it easy to correct, never present it with false certainty.
4. **Logging should cost almost nothing.** The log is valuable only if people keep adding to it.
