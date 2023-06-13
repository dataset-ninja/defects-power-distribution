# https://zenodo.org/record/3972451#.YkWxBn9Bzmg

import os

import numpy as np
import supervisely as sly

# from dotenv import load_dotenv
from supervisely.io.fs import file_exists, get_file_ext, get_file_name

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "Defects in Power Distribution Components"
# dataset_path = "/home/alex/DATASETS/TODO/Defects in Power Distribution Components/Electricity Components Defects"
dataset_path = "./APP_DATA/Electricity Components Defects"
batch_size = 30
ds_name = "ds"

idx_to_obj_class = {
    0: sly.ObjClass("Cable out of spacer", sly.Rectangle),
    1: sly.ObjClass("Cable out of insulator", sly.Rectangle),
    2: sly.ObjClass("Insulator withour ring", sly.Rectangle),
}

obj_classes = list(idx_to_obj_class.values())


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    bbox_name = get_file_name(image_path) + ".txt"
    bbox_path = os.path.join(dataset_path, bbox_name)
    if file_exists(bbox_path):
        with open(bbox_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    curr_data = list(map(float, curr_data.split(" ")))
                    obj_class = idx_to_obj_class[int(curr_data[0])]

                    left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                    right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                    top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                    bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes)
    api.project.update_meta(project.id, meta.to_json())

    all_data = os.listdir(dataset_path)

    images_names = [file_name for file_name in all_data if get_file_ext(file_name) == ".jpg"]

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(dataset_path, image_name) for image_name in img_names_batch
        ]
        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]
        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))

    return project
