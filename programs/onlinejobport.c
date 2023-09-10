#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 100
#define MAX_JOBS 100

struct User {
    char username[20];
    char password[20];
    struct Job {
        char title[50];
        char description[200];
    } jobs[MAX_JOBS];
    int jobCount;
};

struct User users[MAX_USERS];
int userCount = 0;

void registerUser() {
    printf("Registration\n");
    printf("Username: ");
    scanf("%s", users[userCount].username);
    printf("Password: ");
    scanf("%s", users[userCount].password);
    users[userCount].jobCount = 0;
    userCount++;

    FILE *file = fopen("users.txt", "a");
    if (file != NULL) {
        fprintf(file, "%s %s\n", users[userCount - 1].username, users[userCount - 1].password);
        fclose(file);
    }
    printf("Registration successful!\n");
}

int loginUser() {
    printf("Login\n");
    char username[20], password[20];
    printf("Username: ");
    scanf("%s", username);
    printf("Password: ");
    scanf("%s", password);

    FILE *file = fopen("users.txt", "r");
    if (file != NULL) {
        char fileUsername[20], filePassword[20];
        while (fscanf(file, "%s %s", fileUsername, filePassword) != EOF) {
            if (strcmp(username, fileUsername) == 0 && strcmp(password, filePassword) == 0) {
                fclose(file);
                printf("Login successful!\n");
                return 1;
            }
        }
        fclose(file);
    }

    printf("Invalid username or password!\n");
    return 0;
}

void postJob(int userIndex) {
    printf("Post a Job\n");
    if (userIndex == -1) {
        printf("Please login before posting a job.\n");
        return;
    }

    struct User *user = &users[userIndex];
    printf("Title: ");
    getchar();  // Clear the input buffer
    fgets(user->jobs[user->jobCount].title, sizeof(user->jobs[user->jobCount].title), stdin);
    printf("Description: ");
    fgets(user->jobs[user->jobCount].description, sizeof(user->jobs[user->jobCount].description), stdin);
    user->jobCount++;

    char fileName[20];
    sprintf(fileName, "%s_jobs.txt", user->username);
    FILE *file = fopen(fileName, "a");
    if (file != NULL) {
        fprintf(file, "%s\n%s\n", user->jobs[user->jobCount - 1].title, user->jobs[user->jobCount - 1].description);
        fclose(file);
    }
    printf("Job posted successfully!\n");
}

void updateJob(int userIndex) {
    printf("Update Job\n");
    if (userIndex == -1) {
        printf("Please login before updating a job.\n");
        return;
    }

    struct User *user = &users[userIndex];
    printf("Enter the job title to update: ");
    char title[50];
    getchar();  // Clear the input buffer
    fgets(title, sizeof(title), stdin);
    title[strcspn(title, "\n")] = '\0';  // Remove newline character

    int i;
    for (i = 0; i < user->jobCount; i++) {
        if (strcmp(title, user->jobs[i].title) == 0) {
            printf("New Title: ");
            fgets(user->jobs[i].title, sizeof(user->jobs[i].title), stdin);
            printf("New Description: ");
            fgets(user->jobs[i].description, sizeof(user->jobs[i].description), stdin);

            char fileName[20];
            sprintf(fileName, "%s_jobs.txt", user->username);
            FILE *file = fopen(fileName, "w");
            if (file != NULL) {
                int j;
                for (j = 0; j < user->jobCount; j++) {
                    fprintf(file, "%s\n%s\n", user->jobs[j].title, user->jobs[j].description);
                }
                fclose(file);
            }

            printf("Job updated successfully!\n");
            return;
        }
    }
    printf("Job not found!\n");
}

void displayJobs(int userIndex) {
    printf("Jobs List:\n");
    if (userIndex == -1) {
        printf("Please login to view jobs.\n");
        return;
    }

    struct User *user = &users[userIndex];
    char fileName[20];
    sprintf(fileName, "%s_jobs.txt", user->username);
    FILE *file = fopen(fileName, "r");
    if (file != NULL) {
        char title[50], description[200];
        while (fgets(title, sizeof(title), file) != NULL && fgets(description, sizeof(description), file) != NULL) {
            title[strcspn(title, "\n")] = '\0';  // Remove newline character
            description[strcspn(description, "\n")] = '\0';  // Remove newline character
            printf("Title: %s\n", title);
            printf("Description: %s\n\n", description);
        }
        fclose(file);
    }
}

void displayMenu() {
    printf("\nMenu:\n");
    printf("1. Register\n");
    printf("2. Login\n");
    printf("3. Post a Job\n");
    printf("4. Update a Job\n");
    printf("5. Display Jobs\n");
    printf("6. Exit\n");
    printf("Select an option: ");
}

int main() {
    int choice;
    int userIndex = -1; // Index of the logged-in user
    do {
        displayMenu();
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                registerUser();
                break;
            case 2:
                if (userIndex == -1)
                    userIndex = loginUser();
                else
                    printf("Already logged in!\n");
                break;
            case 3:
                postJob(userIndex);
                break;
            case 4:
                updateJob(userIndex);
                break;
            case 5:
                displayJobs(userIndex);
                break;
            case 6:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid option!\n");
        }
    } while (choice != 6);

    return 0;
}
