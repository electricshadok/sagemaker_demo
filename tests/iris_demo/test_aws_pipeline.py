from aws_pipeline.iris_demo.pipeline_setup import pipeline_setup


def test():
    # build the aws stagemaker pipeline without pushing/running it
    pipeline_setup(data_pipeline=True, model_pipeline=True, update=False, start=False)


if __name__ == "__main__":
    test()
