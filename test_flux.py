import torch
#from diffusers import FluxPipeline
from flux_comfy_pipeline import FluxPipeline
from inspector import get_valid_samplers

from k_diffusion import sampling

# HACK: we need to patch to_d, flux models don't need to go from
# predicted noise to denoised.
sampling.to_d = lambda x, sigma, model_output: model_output

# 1m30, 5sec/it

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe = pipe.to("cuda")
#pipe.enable_model_cpu_offload() #save some VRAM by offloading the model to CPU. Remove this if you have enough GPU power

# We need to patch the scheduler and save the original list of sigmas
pipe.scheduler.sigmas_original = pipe.scheduler.sigmas.clone().cpu().numpy()

comfy_samplers = get_valid_samplers()

#prompt = "A cat holding a sign that says hello world"
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"

for sampler_name in comfy_samplers:

    print(f"generating with {sampler_name} ...")

    image = pipe(
        prompt,
        height=512,
        width=512,
        guidance_scale=3.5,
        num_inference_steps=20,
        max_sequence_length=512,
        generator=torch.Generator("cpu").manual_seed(0),
        comfy_sampler=sampler_name
    ).images[0]
    image.save(f"output/flux-dev-{sampler_name}.png")