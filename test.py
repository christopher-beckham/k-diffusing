#from diffusers import StableDiffusionXLPipeline
from sdxl_comfy_pipeline import StableDiffusionXLPipeline
import torch
from inspector import get_valid_samplers

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16, 
    variant="fp16", 
    use_safetensors=True
)
pipe.to("cuda")

# We need to patch the scheduler and save the original list of sigmas
pipe.scheduler.sigmas_original = pipe.scheduler.sigmas.clone().cpu().numpy()

comfy_samplers = get_valid_samplers()

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"

for sampler_name in comfy_samplers:

    print(f"generating with {sampler_name} ...")

    image = pipe(prompt=prompt, comfy_sampler=sampler_name).images[0]
    image.save(f"output/sdxl-{sampler_name}.png")