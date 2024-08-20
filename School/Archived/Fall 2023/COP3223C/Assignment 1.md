# Problem A - Grade Calculator
```C
/*

    Dylan Vidal

    COP3223H

    Section 0204

    Assignment 1 - Problem A - Grade Calculator

    Date: 8/21/2023

  

    Input: gradeCurrent, finalWeight, gradeDesired

  

    Processing: 1. Prompt the user for inputs

                2. Assign inputs to variables

                3. Perform necessary arithmetic on variables to determine the final exam grade needed for target grade

                4. Display the output result

  

    Output: examScore

*/

#include <stdio.h>

  
  

// Main Function

int main() {

  

    // Programming Intro

    printf("\nGrade Calculator Program. . .\n");

    // Declare Necessary Variables

    double gradeCurrent, finalWeight, gradeDesired;

    // Prompt for Current Grade

    printf("\nWhat is your percentage in the class, w/o the final exam?\n");

    scanf("%lf", &gradeCurrent);

  

    // Prompt for Weight of the Final Exam

    printf("What percentage of the final grade is the final exam?\n");

    scanf("%lf", &finalWeight);

  

    // Prompt for the Desired Grade

    printf("What final percentage do you want to achieve for the class?\n");

    scanf("%lf", &gradeDesired);

  

    // Perform Necessary Calculations

    double examScore;

    //Calculate the difference between the Desired Grade and Current Grade, factoring in its current weight, being inverse of the final weight. Then divide by the final Weight.

    examScore = ((100 * gradeDesired) - ((100 - finalWeight) * gradeCurrent)) / (float)finalWeight;

    // Display Results

    printf("You need to score %.9f%% on the final exam to earn your target average.", examScore);

  

    return 0;

}
```

# Problem B - Recipe Adjustment
```C
/*

    Dylan Vidal

    COP3223H

    Section 0204

    Assignment 1 - Problem B - Recipe Adjustments

    Date: 8/21/2023

  

    Input: peopleRecipe, ingredientQuantity, ingredientCost, ingredientOnHand, peopleTarget

  

    Processing: 1. Prompt the user for inputs

                2. Assign inputs to variables

                3. Perform necessary arithmetic on variables to determine the amount of ingredient needed, and the cost\

                4. Display the output result

  

    Output: ingredientNeeded, purchasingCost

*/

#include <stdio.h>

  
  

// Main Function

int main () {

    // Program Intro

    printf("Recipe Adjustment Program. . .\n");

  

    // Declare Necessary Variables

    double peopleRecipe, ingredientQuantity, ingredientCost, ingredientOnHand, peopleTarget;

  

    // Prompt for Number of People of Recipe

    printf("\nHow many people is your recipe for?\n");

    scanf("%lf", &peopleRecipe);

  

    // Prompt for the Quantity of the Ingredient per Recipe

    printf("How much of ingredient X does the recipe call for?\n");

    scanf("%lf", &ingredientQuantity);

  

    // Prompt for the Cost of One Unit of the Ingredient

    printf("What is the cost in dollars of 1 unit of ingredient X?\n");

    scanf("%lf", &ingredientCost);

  

    // Prompt for the Amount of Ingredient on Hand

    printf("How many units of ingredient X do you have now?\n");

    scanf("%lf", &ingredientOnHand);

  

    // Prompt for the Target Number of People Eating

    printf("How many people are you cooking for?\n");

    scanf("%lf", &peopleTarget);

  

    // Perform Necessary Calculations

    double ingredientNeeded, purchasingCost;

  

    // Convert the people ratio into a scalar and apply to quantity needed. Then remove any ingredient on hand.

    ingredientNeeded = ((peopleTarget/peopleRecipe) * ingredientQuantity) - ingredientOnHand;

    // To find the cost of purchasing new ingredients, simply multiply by the cost

    purchasingCost = ingredientNeeded * ingredientCost;

  

    // Display Results

    printf("You need to buy %.3f units of the ingredient X.", ingredientNeeded);

    printf("\nBuying this amount will cost you $%.3f.", purchasingCost);    

  

    return 0;

}
```
