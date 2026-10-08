# Build A DataBase For Models
models_db = []

# Project Structure
while True:
    # Show Menu
    print("Menu\n", 20 * "-", sep="")
    option = input("""1-Add A Model
2-Show All Models
3-Best Model
4-Search By A Filter
5-Show Performance Classification
6-Show Unique Frameworks
7-Model Summary
8-Exit
: """)

    # Core

    # Add A Model
    if option == "1":
        name = input("Enter The Model's Name: ")
        model_type = input("Enter The Type Of Model: ")
        accuracy = float(input("Enter The Accuracy: "))
        framework = input("Enter The Framework: ")
        model_info = {
        "name": name,
        "type": model_type,
        "accuracy": accuracy,
        "framework": framework
        }
        # Add To DataBase
        models_db.append(model_info)
        print("Model Added Successfully.")
        print(20 * "-")


    # Show All Models
    elif option == "2":
        if len(models_db) == 0:
               print("There Is No Model In DataBase Yet, Please Add A Model.")
        else:
               print("All Models\n", 20 * "-", sep="")
               for model in models_db:
                      print(f"""{model["name"]} | {model["accuracy"]} | {model["framework"]}""")
               print(20 * "-")
    
    # Best Model
    elif option == "3":
            if len(models_db) == 0:
                print("There Is No Model In DataBase Yet, Please Add A Model.")
            else:
                best_models = []
                for model in models_db:
                    if len(best_models) == 0:
                          best_models.append(model)
                    elif model["accuracy"] > best_models[0]["accuracy"]:
                            best_models.clear()
                            best_models.append(model)
                    elif model["accuracy"] == best_models[0]["accuracy"]:
                            best_models.append(model)
                best_models_name = []
                for model in best_models:
                    best_models_name.append(model["name"])
                print(20 * "-")
                print(f"""Best Model: {" and ".join(best_models_name)}""")
                print(f"Accuracy: {best_models[0]["accuracy"]}")
                print(20 * "-")
    
    # Search By A Filter
    elif option == "4":
            if len(models_db) == 0:
                print("There Is No Model In DataBase Yet, Please Add A Model.")
            else:
                minimum_accuracy = float(input("Enter Minimum Accuracy: "))
                result = [
                      model
                      for model in models_db
                      if model["accuracy"] >= minimum_accuracy
                ]
                print(20 * "-")
                print(f"Models With Minimum Accuracy = {minimum_accuracy}:")
                if len(result) == 0:
                      print(f"There Is No Model With Minimum Accuracy = {minimum_accuracy}")
                else:
                  for model in result:
                        print(f"""{model["name"]} | {model["accuracy"]} | {model["framework"]}""")
                print(20 * "-")
    
    # Show Performance Classification
    elif option == "5":
            if len(models_db) == 0:
                print("There Is No Model In DataBase Yet, Please Add A Model.")            
            else:      
                  performance = []
                  for model in models_db:
                        if model["accuracy"] >= 0.9:
                              performance.append(f"{model["name"]} → Good")
                        elif 0.7 < model["accuracy"] < 0.9:
                              performance.append(f"{model["name"]} → Needs Improvement")
                        else:
                              performance.append(f"{model["name"]} → Bad")
                  print(20 * "-")
                  print("Models Performance:")
                  for item in performance:
                        print(item)
                  print(20 * "-")

    # Show Unique Frameworks
    elif option == "6":
            if len(models_db) == 0:
                print("There Is No Model In DataBase Yet, Please Add A Model.")
            else:            
                  frameworks = {
                        model["framework"]
                        for model in models_db
                  }
                  print(20 * "-")
                  print("Frameworks: ")
                  for item in frameworks:
                        print(item)
                  print(20 * "-")
      
    # Model Summary
    elif option == "7":
            if len(models_db) == 0:
                print("There Is No Model In DataBase Yet, Please Add A Model.")
            else:            
                  total_models = len(models_db)

                  best_models = []
                  for model in models_db:
                        if len(best_models) == 0:
                                    best_models.append(model)
                        elif model["accuracy"] > best_models[0]["accuracy"]:
                                    best_models.clear()
                                    best_models.append(model)
                        elif model["accuracy"] == best_models[0]["accuracy"]:
                                    best_models.append(model)
                  best_models_name = []
                  for model in best_models:
                        best_models_name.append(model["name"])
                  best_accuracy = best_models[0]["accuracy"]

                  high_performance_models = [
                        model["name"]
                        for model in models_db
                        if model["accuracy"] >= 0.9
                  ]
            
                  frameworks = {
                        model["framework"]
                        for model in models_db
                  }

                  print(20 * "-")
                  print("===== AI MODEL SUMMARY =====\n")

                  print(f"Total Models: {total_models}")
                  print(f"""Best Model: {" and ".join(best_models_name)}""")
                  print(f"Best Accuracy: {best_accuracy}\n")

                  print("High Performance Models:")
                  for model in high_performance_models:
                        print(model)

                  print("\nFrameworks:")
                  for framework in frameworks:
                        print(framework)
                  print(20 * "-")
            
    # Exit
    elif option == "8":
            print("Have A Good Time.")
            break
    
    # Invalid Answers
    else:
           print("Invalid Answer! Please Try Again.")
